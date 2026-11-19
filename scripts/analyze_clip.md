# Video Analyzer Usage

`analyze_clip.py` measures an existing video and can produce a JSON report and a contact sheet. It helps locate candidate cuts and changes in pixel motion. It does not generate or edit the input video, identify characters, track their paths, judge acting, listen to audio, or verify lip sync.

## Requirements

- Python 3 with the standard library; no pip packages are required.
- `ffmpeg` and `ffprobe` available on `PATH` in the same terminal that runs Python.
- A readable local video file. The analyzer selects the first video stream.

Check the tools in PowerShell:

```powershell
python --version
ffmpeg -version
ffprobe -version
```

If a command is missing, install or locate that tool using your normal software setup and make it available on `PATH`. Merely placing FFmpeg in an unrelated folder does not make the command discoverable.

## Quick start

From the skill folder:

```powershell
python scripts/analyze_clip.py "C:\Videos\fight clip.mp4"
```

This prints the JSON report to the terminal. Without output options, it creates no report or image files.

To run from any working directory, use the script's absolute path and save outputs in a project review folder:

```powershell
$skill = "C:\Tools\ai-video-prompts"
$video = "C:\Videos\fight clip.mp4"
$review = "C:\Projects\scene-review"

python "$skill\scripts\analyze_clip.py" "$video" --json "$review\metrics.json" --sheet "$review\contact.png"
```

Replace these example paths with your actual locations. Quotes preserve paths containing spaces. Output parent folders are created automatically. Keep generated reports and images in project work, outside the installed skill.

For macOS or Linux, from the unpacked skill folder:

```sh
python3 scripts/analyze_clip.py "/path/to/fight clip.mp4" --json "/path/to/review/metrics.json" --sheet "/path/to/review/contact.png"
```

## Command options

| Argument | Required | Behavior |
|---|---|---|
| `clip` | Yes | Path to the existing input video |
| `--json PATH` | No | Writes the same JSON report that is printed to the terminal |
| `--sheet PATH` | No | Writes a contact sheet; a `.png` filename is the recommended example format |
| `-h`, `--help` | No | Prints command help and exits |

The input and both outputs must resolve to different files. Specified existing output files are overwritten; the source video is protected from being used as an output. Relative paths resolve from the terminal's current working directory, not from the script folder.

## Reading the report

| Field | Meaning and practical limit |
|---|---|
| `duration` | File duration reported by FFprobe, in seconds; not proof that a damaged file decodes completely |
| `width`, `height` | Dimensions of the first video stream |
| `fps` | The stream's reported `r_frame_rate`, rounded to three decimals; not a frame-by-frame variable-rate analysis |
| `cuts` | Candidate cut timestamps in seconds at FFmpeg scene thresholds `0.08`, `0.15`, and `0.25`; a lower threshold is more sensitive |
| `energy_per_second` | Mean absolute grayscale pixel difference after sampling at 8 fps and 160 x 90 pixels, grouped into approximately one-second bins; the final bin can be partial |
| `median` | Median of those motion-energy bins |
| `peaks_at_s`, `peak_count` | Strong local motion-bin peaks and their count; the listed bin indices are approximate seconds, not exact contact or choreography timestamps |
| `stillness_ratio` | Fraction of relatively quiet interior bins; for clips with more than six bins, the first and last two are omitted. Camera motion, lighting and editing also affect this value |
| `end_hold_s` | Coarse estimate of trailing low-motion bins, capped at the probed duration; partial bins make this an estimate |
| `dynamic_range_p90_over_p10` | Relative spread of the energy bins, using a small denominator floor; not a quality score or an intensity measurement in physical units |
| `measurement_scope` | Reminder that pixel measurements do not certify actor movement, performance, audio or sync |

A bright effect, flash, exposure change or fast camera move may create a cut candidate. Camera travel can raise motion energy while the actors remain planted. Compare timestamps with actual frames and continuous playback before drawing a conclusion. Review audio separately by listening.

The contact sheet targets 6 to 120 evenly spaced thumbnails, arranged in four columns with 480-pixel-wide cells. The last row can contain padding. It helps locate moments; it cannot establish the path, speed or contact order between sampled frames.

For a three-second synthetic clip that switches from black to white at one second and back to black at two seconds, a verified example is:

```json
{
  "duration": 3.0,
  "width": 64,
  "height": 64,
  "fps": 8.0,
  "cuts": {
    "0.08": [1.0, 2.0],
    "0.15": [1.0, 2.0],
    "0.25": [1.0, 2.0]
  }
}
```

This is a small excerpt from a tool test, not the expected result for an arbitrary fight video. Development fixtures are not required to use the analyzer and are not shipped in the runtime package.

## Errors and exit codes

| Symptom | Action |
|---|---|
| `Input video does not exist` | Check the path, extension and quoting |
| Executable-not-found error | Check that both FFmpeg and FFprobe are discoverable in this terminal |
| `Input has no video stream`, invalid-data or decode error | Check that this is a readable video; container metadata alone does not prove valid footage |
| Input/output paths are not distinct | Choose separate JSON and PNG output paths |
| Timeout | The per-subprocess limit is 120 seconds. Review a shorter source selection or investigate a slow/damaged input |
| Output access or format error | Choose a writable project folder and a supported image extension, such as `.png` |

Exit code `0` means the requested analysis completed. Exit code `2` means invalid arguments, missing/invalid input, unavailable tools or another handled analysis failure; read the terminal message. The script makes multiple decoding passes, and grayscale-frame memory grows with duration, so it is intended for manageable review clips rather than unattended full-film analysis.
