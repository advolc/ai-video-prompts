from pathlib import Path
import copy, json, subprocess, sys, runpy
r=Path(__file__).resolve().parents[1]
analyze=runpy.run_path(str(r/'scripts/check_spatial.py'))['analyze']
checks=[]
def check(name,condition):
    assert condition,name
    checks.append(name)
for f in (r/'scripts').glob('*.py'):
    compile(f.read_text(encoding='utf-8-sig'),str(f),'exec')
    checks.append('syntax: '+f.name)
base={'mode':'duel','runtime_s':10,'arena':{'has_height':True,'landmarks':[{'id':'r1'},{'id':'r2'}]},'beats':[]}
for t,ap,bp in [(0,(0,0,1),(2,0,0)),(5,(0,2,1),(-2,2,0)),(10,(2,2,1),(2,0,0))]:
    base['beats'].append({'t':t,'A':dict(zip(['x','y','z'],ap),facing=0,anchor='r1'),'B':dict(zip(['x','y','z'],bp),facing=0,anchor='r2'),'answer':'arc'})
result=analyze(base)
check('different actors heights are not temporal change',result['metrics']['max_individual_height_range_bl']==0)
check('different actors anchors are not temporal change',result['metrics']['anchor_changes']==0)
hold=copy.deepcopy(base)
for b in hold['beats']:b['A']=copy.deepcopy(hold['beats'][0]['A']);b['B']=copy.deepcopy(hold['beats'][0]['B'])
check('valid fixed doorway has no movement quota',analyze(hold)['status']=='VALID_DESIGN_DATA')
hold['requirements']={'min_height_change_bl':0.5,'min_anchor_changes':1}
check('explicit height and anchor targets fail when absent',len(analyze(hold)['unmet_requirements'])==2)
hold['beats'][-1]['A']['z']+=1
hold['beats'][-1]['A']['anchor']='r2'
check('actual individual changes meet requested targets',not analyze(hold)['unmet_requirements'])
for label,mut in [
('empty beats',lambda x:x.update(beats=[])),
('duplicate time',lambda x:x['beats'][1].update(t=0)),
('NaN coordinate',lambda x:x['beats'][0]['A'].update(x=float('nan'))),
('missing facing',lambda x:x['beats'][0]['A'].pop('facing')),
('unknown anchor',lambda x:x['beats'][0]['A'].update(anchor='missing')),
('negative runtime',lambda x:x.update(runtime_s=-1)),
('unknown requirement',lambda x:x.update(requirements={'madeup':1})),
('bool coordinate',lambda x:x['beats'][0]['A'].update(x=True))]:
    bad=copy.deepcopy(base);mut(bad)
    try:analyze(bad)
    except ValueError:checks.append('reject '+label)
    else:raise AssertionError(label)
coincident=copy.deepcopy(base);coincident['beats'][0]['B']=copy.deepcopy(coincident['beats'][0]['A'])
check('undefined bearing reported honestly',analyze(coincident)['metrics']['bearing_sweep_deg'] is None)
def lint(text,*args):
    return subprocess.run([sys.executable,'-X','utf8','-B',str(r/'scripts/lint_prompt.py'),'-',*args],input=text,text=True,capture_output=True,encoding='utf-8')
for label,text in [('clothing seam','The seam of his coat splits as he lifts his arm.'),('English dialogue','Chen says, "There is tension between us. Do not lie to me."'),('Chinese dialogue','甲说：“我不能告诉你。”乙沉默地望着他。'),('single quotes',"Chen says, 'There is tension. Do not move.'")]:
    out=lint(text);check(label,out.returncode==0 and 'ERROR' not in out.stdout)
check('real production label detected',lint('GEN_01\nCamera: close').returncode==1)
check('verified platform structure supported',lint('SHOT 1\nCamera: close','--format','platform').returncode==0)
check('short output does not need padding','do not pad' in lint('He holds the door.').stdout)
ls=(r/'examples/v3-extended-examples.md').read_text(encoding='utf-8').splitlines();blocks=[];cur=[]
for l in ls+['']:
    if l.startswith('>'):cur.append(l[2:])
    elif cur:blocks.append('\n'.join(cur));cur=[]
for i,b in enumerate(blocks):check('example lint '+str(i+1),lint(b).returncode==0)

import tempfile
rr=runpy.run_path(str(r/'scripts/read_route.py'))
collect,section=rr['collect'],rr['section']
manifest=json.loads((r/'assets/routes.json').read_text(encoding='utf-8'))
for route in manifest['routes']:
    items=collect(r,[route])
    check('route resolves: '+route,bool(items) and all(e['heading'] in t for e,t in items))
combined=collect(r,['action','dialogue'])
check('mixed routes deduplicate shared sections',len(combined)<len(collect(r,['action']))+len(collect(r,['dialogue'])))
try:collect(r,['missing'])
except ValueError:checks.append('unknown route rejected')
else:raise AssertionError('unknown route accepted')
with tempfile.TemporaryDirectory() as folder:
    root=Path(folder);(root/'chapter.md').write_text('# Book\n## Selected\nKEEP\n### Child\nCHILD\n## Other\nOMIT\n',encoding='utf-8')
    selected=section(root,{'path':'chapter.md','heading':'## Selected'})
    check('section preserves children and excludes siblings','CHILD' in selected and 'OMIT' not in selected)
    for entry in [{'path':'../outside.md','heading':'## X'},{'path':'chapter.md','heading':'## Missing'}]:
        try:section(root,entry)
        except ValueError:checks.append('unsafe or stale section rejected')
        else:raise AssertionError('invalid section accepted')
for key,entry in json.loads((r/'assets/owners.json').read_text(encoding='utf-8')).items():
    section(r,entry)
checks.append('all rule owners resolve')
# Confirm structural validation rejects real broken registries and unreachable sources.
import shutil
with tempfile.TemporaryDirectory() as folder:
    clone=Path(folder)/'skill'
    shutil.copytree(r,clone,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    owners_path=clone/'assets/owners.json'
    original=owners_path.read_text(encoding='utf-8')
    broken=json.loads(original)
    broken['speech_pace']['heading']='## Missing canonical source'
    owners_path.write_text(json.dumps(broken),encoding='utf-8')
    outcome=subprocess.run([sys.executable,'-X','utf8','-B',str(clone/'scripts/check_skill.py'),str(clone)],capture_output=True,text=True,encoding='utf-8')
    check('structural checker rejects broken owner',outcome.returncode==1 and 'route/owner registry' in outcome.stdout)
    owners_path.write_text(original,encoding='utf-8')
    (clone/'references/unreachable.md').write_text('# Unreachable reference\n\n'+('Useful but undiscoverable content. '*8),encoding='utf-8')
    outcome=subprocess.run([sys.executable,'-X','utf8','-B',str(clone/'scripts/check_skill.py'),str(clone)],capture_output=True,text=True,encoding='utf-8')
    check('structural checker rejects unreachable reference',outcome.returncode==1 and 'unreachable from entrypoint' in outcome.stdout)

# Exercise the documented first-use commands unchanged from a fresh project copy.
import re, shlex
with tempfile.TemporaryDirectory() as folder:
    fresh=Path(folder)/'fresh extraction with spaces'/'ai-video-prompts'
    shutil.copytree(r,fresh,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    readme=(fresh/'README.md').read_text(encoding='utf-8')
    first_use=readme.split('## First use',1)[1].split('## Tools',1)[0]
    commands=re.search(r'```text\n(.*?)```',first_use,re.S).group(1).strip().splitlines()
    for i,line in enumerate(commands):
        command=shlex.split(line)
        assert command[0]=='python',line
        output=subprocess.run([sys.executable,*command[1:]],cwd=fresh,capture_output=True,text=True,encoding='utf-8')
        check('README first use command '+str(i+1),output.returncode==0)
        if 'lint_prompt.py' in line:
            check('English example counted as English words',bool(re.search(r'length: [1-9][0-9]* words',output.stdout)) and '0 error(s)' in output.stdout)
    output=subprocess.run([sys.executable,'-X','utf8','-B','scripts/read_route.py','action'],cwd=fresh,capture_output=True,text=True,encoding='utf-8')
    check('action route executes from fresh path with spaces',output.returncode==0 and 'SOURCE:' in output.stdout)
check('auto language counts an English input',bool(re.search(r'length: [1-9][0-9]* words',lint('The guard turns the spear aside.','--lang','auto').stdout)))
check('auto language counts a Chinese input',bool(re.search(r'length: [1-9][0-9]* characters',lint('守卫用短棍拨开长矛，身体始终挡住门口。','--lang','auto').stdout)))
check('wrong explicit counting mode stays advisory',lint('The guard holds the doorway.','--lang','zh').returncode==0)

print(json.dumps({'passed':len(checks),'checks':checks},ensure_ascii=False,indent=2))
