`CLAUDE.md` is a configuration file that provides project-specific instructions to Claude Code. It contains general instructions applicable to every coding session.

## Locations

- **Repo root**
- **Parent directories** — useful for monorepos; both `root/CLAUDE.md` and `root/foo/CLAUDE.md` are loaded automatically
- **Child directories** — pulled in on demand when working with files in subdirectories
- **Home folder** (`~/.claude/CLAUDE.md`) — applies globally to all Claude sessions

You can use [[Project Analysis Prompt]] (or `/init`) to generate it.

