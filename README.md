# Awesome Jev [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of tools, integrations, and experiments built on **Jev**, the System One model from [TypeSafe AI](https://typesafe.ai/) that makes fast, typed, confidence-aware decisions.

Jev doesn't write paragraphs. You give it a question and a set of candidates, and it returns a typed answer with a confidence score, in milliseconds and for fractions of a cent. That makes it a good fit for work that needs many small decisions in a loop: picking the next click in a browser or on a phone, routing a task to the right model, classifying documents, scoring code changes, or deciding whether to trade.

**No waitlist needed:** Jev is available through [Vercel AI Gateway](https://vercel.com/ai-gateway) as `typesafe-ai/jev`.

Within each section, projects are sorted by GitHub stars. Counts are refreshed weekly by [a workflow](.github/workflows/stars.yml).

## Contents

- [Official resources](#official-resources)
- [Browser & computer use](#browser--computer-use)
- [Mobile & robotics](#mobile--robotics)
- [Coding agents & developer tools](#coding-agents--developer-tools)
- [MCP servers & agent skills](#mcp-servers--agent-skills)
- [Data, search & classification](#data-search--classification)
- [Trading](#trading)
- [Games & fun](#games--fun)
- [Open models & replications](#open-models--replications)
- [Other lists](#other-lists)

## Official resources

- [TypeSafe AI](https://typesafe.ai/) - Product site for System One models and Jev.
- [Documentation](https://docs.typesafe.ai/) - Guides, SDK references, patterns, and the HTTP API.
- [Quick start](https://docs.typesafe.ai/introduction/quickstart) - From an API key to your first typed decision in Python or JavaScript.
- [Primitives](https://docs.typesafe.ai/primitives) - Choice, Score, and Noul, and when to use each.
- [Patterns](https://docs.typesafe.ai/patterns) - Confidence-gated routing, composite scoring, speculative fan-out, intent routing.
- [TypeSafe Console](https://console.typesafe.ai/) - API keys and live request inspection.
- [Workflow evals](https://evals.typesafe.ai/) - Published workflows, model comparisons, and methodology.
- [skills](https://github.com/typesafe-ai/skills) - Official agent skills for designing TypeSafe workflows from Claude Code, Codex, and similar agents. ⭐ 270
- [typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) - Official TypeScript/JavaScript SDK with inferred answer types. ⭐ 128
- [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) - Drop-in `TypeSafeClient` replacement backed by regular LLM APIs, handy for local testing. ⭐ 121
- [typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) - Official sync and async Python SDK. ⭐ 87

## Browser & computer use

- [trycua/cua](https://github.com/trycua/cua/tree/main/libs/cua-driver/examples/jev-use) - Open-source computer-use platform with cross-OS drivers. Its `jev-use` example lets Jev choose the next action. ⭐ 23.4k
- [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) - Browser agent that uses Jev to pick target elements and only calls a small LLM when it has to type text. ⭐ 5.6k
- [awlevin/typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) - macOS computer use for about $0.0002 a step: OCR the screen, let Jev pick the next click. ⭐ 223
- [socai-io/socai](https://github.com/socai-io/socai) - Browser and computer-use agent tuned for social media research and content extraction. ⭐ 190
- [jkudish/jev-browser](https://github.com/jkudish/jev-browser) - Browser automation driven by Jev. ⭐ 105
- [wy-coliney/jev-browser-use](https://github.com/wy-coliney/jev-browser-use) - Jev handles the clicks while Codex plans and verifies, for 5-10x faster browser runs. ⭐ 101
- [kitze/unclutter](https://github.com/kitze/unclutter) - Browser extension that uses Jev to strip page clutter, with reusable template rules. ⭐ 99
- [moritzkremb/jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser) - Voice-controlled browser. Jev resolves intent and target in about 300 ms per spoken word, and Playwright executes. ⭐ 75
- [jcpsimmons/jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop) - Native macOS GUI automation on Apple silicon: OmniParser CoreML and Apple Vision OCR find the controls, and Jev picks the action. ⭐ 2

## Mobile & robotics

- [rokbenko/quackd](https://github.com/rokbenko/quackd) - One CLI for many robots (Open Duck Mini, LeRobot, ToddlerBot, ROS bases). An LLM does the planning and Jev handles the cheaper steps. ⭐ 211
- [droidrun/mobile-jev](https://github.com/droidrun/mobile-jev) - Agent that drives real Android devices with Jev. Includes live demos, a CLI, and execution traces. ⭐ 137

## Coding agents & developer tools

- [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) - Claude Code plugin that replaces compaction summaries with Jev decisions. Each tool call is scored, stale ones are dropped, and the rest stays verbatim. ⭐ 3.2k
- [thruwire/foreman](https://github.com/thruwire/foreman) - Software factory "foreman" built on Jev. ⭐ 298
- [devagrawal09/jev-review](https://github.com/devagrawal09/jev-review) - Staged code review over git diffs or whole codebases, scoring correctness, safety, reliability, compatibility, and test risk in a local dashboard. ⭐ 269
- [gargpratyush/jev-router](https://github.com/gargpratyush/jev-router) - Routes each Claude Code or Codex turn: easy tasks go to fast models, hard ones to strong models. ⭐ 140
- [NiazMorshed2007/jev-review](https://github.com/NiazMorshed2007/jev-review) - Local-first MCP plugin for continuous quality review by AI coding agents. ⭐ 122
- [vinilana/jev-eval-agent](https://github.com/vinilana/jev-eval-agent) - Evaluation agent built on Jev. ⭐ 85
- [mrnugget/jev-shell-history](https://github.com/mrnugget/jev-shell-history) - Fish-style zsh history autosuggestions ranked by Jev. ⭐ 43
- [EliaAlberti/jev-rules](https://github.com/EliaAlberti/jev-rules) - Claude Code plugin where Jev picks which of your rules apply to each prompt, so Claude only sees the relevant ones. ⭐ 9
- [morcoan/JevSeek](https://github.com/morcoan/JevSeek) - Local coding workspace: Jev routes actions and DeepSeek generates arguments. Native tools, persistent sessions, React desktop app. ⭐ 2

## MCP servers & agent skills

- [kitze/skillbox](https://github.com/kitze/skillbox) - Self-hosted, versioned skills library for AI agents with optional Jev recommendations. ⭐ 161
- [dbreunig/building-with-jev-skill](https://github.com/dbreunig/building-with-jev-skill) - Agent skill for writing and improving programs that call Jev. ⭐ 104
- [jkudish/jev-mcp](https://github.com/jkudish/jev-mcp) - Fast, cheap, typed judgments from Jev as MCP tools. ⭐ 73
- [itsmostafa/typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp) - MCP connector that gives any agent direct access to Jev. ⭐ 69

## Data, search & classification

- [realZachi/pg-jev](https://github.com/realZachi/pg-jev) - PostgreSQL extension for asking your tables questions in plain language. ⭐ 166
- [kyotofin/tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) - Tax document page classifier. Reports 100% strict accuracy on 261 IRS forms at about $0.001 per page. ⭐ 121
- [superagents-lab/jev-search](https://github.com/superagents-lab/jev-search) - Web search with Jev handling source selection, query understanding, and relevance ranking. ⭐ 113
- [giuliosmall/pg_typesafe](https://github.com/giuliosmall/pg_typesafe) - Pre-alpha PostgreSQL extension for categorical classification with Jev. ⭐ 76
- [ChetasLua/jevmeter](https://github.com/ChetasLua/jevmeter) - Scores every sentence of a video with Jev and renders a live meter on a 16:9 edit. ⭐ 56

## Trading

- [jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader) - One buy/sell decision per Monad block on Kuru MON-USDC. Runs in dry-run/mock mode by default and makes no promise of profit. ⭐ 872

> Trading bots can lose money. Read the code and run in dry-run mode first.

## Games & fun

- [fhshaik/typesafe-mario](https://github.com/fhshaik/typesafe-mario) - Jev agent that plays Super Mario Bros. from structured emulator state. ⭐ 262
- [dabit3/jev-experiments](https://github.com/dabit3/jev-experiments) - Assorted Jev experiments. ⭐ 224

## Open models & replications

None of these are the official TypeSafe model. They are independent projects that copy Jev's input/output shape with open weights.

- [TheoLeeCJ/SemIf](https://github.com/TheoLeeCJ/SemIf) - "Semantic ifs" from open models on a single home GPU (3090). Formerly `openjev`. ⭐ 1.6k
- [vinnylarouge/jevlike](https://github.com/vinnylarouge/jevlike) - Trains a Jev-like model on your own data to pick one option from a changing candidate set. More an interesting experiment than a practical tool. ⭐ 891
- [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev) - Nano replica of Jev with parallel decisions, dynamic candidates, and an end-to-end training pipeline. ⭐ 381
- [ekzhang/openjev-sglang](https://github.com/ekzhang/openjev-sglang) - Jev-compatible, prefill-only API endpoint built on open models with SGLang. ⭐ 156
- [jaredpalmer/kev](https://github.com/jaredpalmer/kev) - Tiny Jev-like model on Qwen2.5-0.5B that you can train and run on a MacBook. ⭐ 143
- [hr98w/jev-visual](https://github.com/hr98w/jev-visual) - Educational Jev-like visual inference experiment on Apple Silicon. ⭐ 109
- [iammrduncan/typesafe-ai-benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark) - LLM gateway that imitates TypeSafe's structured output, for benchmarking against the real thing. ⭐ 32

## Other lists

- [Anil-matcha/awesome-jev-by-typesafe](https://github.com/Anil-matcha/awesome-jev-by-typesafe) - Use cases, patterns, prompts, and starter code. ⭐ 523
- [AbdelStark/awesome-typesafe](https://github.com/AbdelStark/awesome-typesafe) - Official resources and community projects for TypeSafe and System One models. ⭐ 224
- [yibie/awesome-jev](https://github.com/yibie/awesome-jev) - Public projects, integrations, and discussions. ⭐ 170
- [cobanov/awesome-jev](https://github.com/cobanov/awesome-jev) - Source-backed list of projects built with Jev. ⭐ 114
- [fatwang2/awesome-jev](https://github.com/fatwang2/awesome-jev) - Project directory plus a reusable Jev-based GitHub review workflow. ⭐ 113

## Contributing

Found something good? Open a pull request. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

This list is released under [CC0 1.0](LICENSE). This project is not affiliated with TypeSafe AI.
