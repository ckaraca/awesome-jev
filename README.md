# Awesome Jev [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of tools, integrations, and experiments built on **Jev**, the System One model from [TypeSafe AI](https://typesafe.ai/) that makes fast, typed, confidence-aware decisions.

Jev doesn't write paragraphs. You give it a question and a set of candidates, and it returns a typed answer with a confidence score, in milliseconds and for fractions of a cent. That makes it a good fit for work that needs many small decisions in a loop: picking the next click in a browser or on a phone, routing a task to the right model, classifying documents, scoring code changes, or deciding whether to trade.

**No waitlist needed:** Jev is available through [Vercel AI Gateway](https://vercel.com/ai-gateway) as `typesafe-ai/jev`.

Within each section, projects are sorted by GitHub stars. Counts are refreshed weekly by [a workflow](.github/workflows/stars.yml). Stars belong to the whole repository, including projects where Jev is one optional integration.

## Contents

- [Official resources](#official-resources)
- [Frameworks & integrations](#frameworks--integrations)
- [Browser & computer use](#browser--computer-use)
- [Mobile & robotics](#mobile--robotics)
- [Coding agents & developer tools](#coding-agents--developer-tools)
- [MCP servers & agent skills](#mcp-servers--agent-skills)
- [Observability](#observability)
- [Data, search & classification](#data-search--classification)
- [Trading](#trading)
- [Games & fun](#games--fun)
- [Apps with Jev inside](#apps-with-jev-inside)
- [Community SDKs](#community-sdks)
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
- [skills](https://github.com/typesafe-ai/skills) - Official agent skills for designing TypeSafe workflows from Claude Code, Codex, and similar agents. ⭐ 2.6k
- [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) - Drop-in `TypeSafeClient` replacement backed by regular LLM APIs, handy for local testing. ⭐ 380
- [typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) - Official TypeScript/JavaScript SDK with inferred answer types. ⭐ 268
- [typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) - Official sync and async Python SDK. ⭐ 267

## Frameworks & integrations

- [ComposioHQ/composio](https://github.com/ComposioHQ/composio) - Python and TypeScript providers that let Jev select tools and bind supported arguments, with partial-call and abstention results. ⭐ 30.4k
- [vercel/ai](https://github.com/vercel/ai) - AI SDK's TypeSafe provider exposes Jev through the experimental evaluation API for typed Choice, Score, and Boolean questions. ⭐ 27.1k
- [0xPlaygrounds/rig](https://github.com/0xPlaygrounds/rig) - Rust agent framework with an experimental `rig-typesafeai` crate for typed Jev judgments. ⭐ 8.8k
- [ax-llm/ax](https://github.com/ax-llm/ax) - DSPy-style framework with TypeSafe/Jev support for boolean and class signatures, plus a native client for probabilities and scoring. ⭐ 3k
- [agentjido/req_llm](https://github.com/agentjido/req_llm) - Elixir library with typed Jev evaluation through TypeSafe or OpenRouter, retaining probability distributions and provider responses. ⭐ 590
- [ash-project/ash_ai](https://github.com/ash-project/ash_ai) - Maps Ash action arguments and return types to Jev evaluation requests through ReqLLM. ⭐ 190
- [donvito/ai-backends](https://github.com/donvito/ai-backends) - API server with a dedicated Jev evaluation endpoint and an interactive playground for typed decisions. ⭐ 146

## Browser & computer use

- [trycua/cua](https://github.com/trycua/cua/tree/main/libs/cua-driver/examples/jev-use) - Open-source computer-use platform with cross-OS drivers. Its `jev-use` example lets Jev choose the next action. ⭐ 28.1k
- [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) - Browser agent that uses Jev to pick target elements and only calls a small LLM when it has to type text. ⭐ 22k
- [awlevin/typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) - macOS computer use for about $0.0002 a step: OCR the screen, let Jev pick the next click. ⭐ 1.2k
- [wy-coliney/jev-browser-use](https://github.com/wy-coliney/jev-browser-use) - Jev handles the clicks while Codex plans and verifies, for 5-10x faster browser runs. ⭐ 896
- [moritzkremb/jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser) - Voice-controlled browser. Jev resolves intent and target in about 300 ms per spoken word, and Playwright executes. ⭐ 385
- [kitze/unclutter](https://github.com/kitze/unclutter) - Browser extension that uses Jev to strip page clutter, with reusable template rules. ⭐ 355
- [jkudish/jev-browser](https://github.com/jkudish/jev-browser) - Browser automation driven by Jev. ⭐ 310
- [socai-io/socai](https://github.com/socai-io/socai) - Browser and computer-use agent tuned for social media research and content extraction. ⭐ 231
- [realZachi/typesafe-adblock](https://github.com/realZachi/typesafe-adblock) - Fun Chrome extension that asks Jev "is this element an ad?" and removes it. BYOK, no backend, not a real ad blocker. ⭐ 89
- [jcpsimmons/jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop) - Native macOS GUI automation on Apple silicon: OmniParser CoreML and Apple Vision OCR find the controls, and Jev picks the action. ⭐ 24
- [valentynkit/jev-skip](https://github.com/valentynkit/jev-skip) - Browser extension that sends YouTube captions to Jev, visualizes segment classifications on the seek bar, and auto-skips high-confidence segments by default. Requires a user-supplied API key; auto-skip can be disabled. ⭐ 7

## Mobile & robotics

- [jev-chat/jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis) - Android chat assistant that uses Jev to assess intent and rank draft replies. Can fill the input field, but sending remains manual; chat context goes to configured providers. ⭐ 7.4k
- [droidrun/mobile-jev](https://github.com/droidrun/mobile-jev) - Agent that drives real Android devices with Jev. Includes live demos, a CLI, and execution traces. ⭐ 433
- [rokbenko/quackd](https://github.com/rokbenko/quackd) - One CLI for many robots (Open Duck Mini, LeRobot, ToddlerBot, ROS bases). An LLM does the planning and Jev handles the cheaper steps. ⭐ 249
- [RomanSlack/jev-drone](https://github.com/RomanSlack/jev-drone) - Camera-only autonomous drone in MuJoCo with Jev in the control loop at 2.5 Hz. ⭐ 248

## Coding agents & developer tools

- [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) - Claude Code plugin that replaces compaction summaries with Jev decisions. Each tool call is scored, stale ones are dropped, and the rest stays verbatim. ⭐ 7.4k
- [dzhng/jevgrep](https://github.com/dzhng/jevgrep) - CLI that uses Jev to find relevant files and source excerpts from natural-language queries. Sends selected source content to the configured hosted provider. ⭐ 2.3k
- [vercel-labs/ai-cli](https://github.com/vercel-labs/ai-cli) - Terminal CLI whose `ai evaluate` command asks typed questions about stdin and returns JSON, using Jev through Vercel AI Gateway by default. ⭐ 820
- [thruwire/foreman](https://github.com/thruwire/foreman) - Software factory "foreman" built on Jev. ⭐ 672
- [devagrawal09/jev-review](https://github.com/devagrawal09/jev-review) - Staged code review over git diffs or whole codebases, scoring correctness, safety, reliability, compatibility, and test risk in a local dashboard. ⭐ 670
- [ksenxx/kiss_ai](https://github.com/ksenxx/kiss_ai) - Agent framework whose optional Jev task classifier decides whether a request needs development work, with an LLM fallback. ⭐ 554
- [coldteadotai/abide](https://github.com/coldteadotai/abide) - Makes your coding agent follow your project rules: Jev checks every edit or turn against each rule in AGENTS.md and returns a probability. ⭐ 543
- [gargpratyush/jev-router](https://github.com/gargpratyush/jev-router) - Routes each Claude Code or Codex turn: easy tasks go to fast models, hard ones to strong models. ⭐ 542
- [notque/vexjoy-agent](https://github.com/notque/vexjoy-agent) - Agent toolkit with a Jev-powered `/d` command for routing requests to agents, skills, and pipelines. ⭐ 424
- [BillionsBobby/JevRouter](https://github.com/BillionsBobby/JevRouter) - Routes requests among models, tools, skills, and subagents using Jev's typed choices. Returns decisions for the host to execute, with CLI, SDK, and MCP interfaces. ⭐ 388
- [WrongStack/WrongStack](https://github.com/WrongStack/WrongStack) - Coding agent with opt-in Jev skill suggestions and fleet-dispatch classification through TypeSafe or OpenRouter. ⭐ 363
- [lakeday-org/perch](https://github.com/lakeday-org/perch) - Semantic code linting with Jev. ⭐ 346
- [SREGym/SREGym](https://github.com/SREGym/SREGym) - Benchmark for incident-resolution agents with optional Jev review of Codex diagnostic tests and submissions, disabled by default. ⭐ 309
- [yonatangross/orchestkit](https://github.com/yonatangross/orchestkit) - Claude Code toolkit with opt-in Jev session classification and workflow routing, including shadow modes and fallbacks. ⭐ 285
- [monotykamary/pi-fabric](https://github.com/monotykamary/pi-fabric) - Pi agent runtime with typed Jev judgments and foreground or background decision loops with explicit budgets. ⭐ 281
- [0xNatoshi/jev-codex-router](https://github.com/0xNatoshi/jev-codex-router) - Per-turn routing for Codex: Jev picks the model, reasoning depth, and speed mode. ⭐ 273
- [NiazMorshed2007/jev-review](https://github.com/NiazMorshed2007/jev-review) - Local-first MCP plugin for continuous quality review by AI coding agents. ⭐ 233
- [DevMortimer/pi-warden](https://github.com/DevMortimer/pi-warden) - Guardrails for Pi: Jev flags irreversible or off-task tool calls, stuck loops, and unverified "done" claims. ⭐ 161
- [y0usaf/pi-jev](https://github.com/y0usaf/pi-jev) - Jev as a decision layer for the Pi coding agent, with a tool-call gate and typed `jev_ask`. ⭐ 157
- [mrnugget/jev-shell-history](https://github.com/mrnugget/jev-shell-history) - Fish-style zsh history autosuggestions ranked by Jev. ⭐ 119
- [vinilana/jev-eval-agent](https://github.com/vinilana/jev-eval-agent) - Evaluation agent built on Jev. ⭐ 106
- [ellipsis-dev/blink](https://github.com/ellipsis-dev/blink) - Codebase search powered by Jev. ⭐ 93
- [IAmUnbounded/save-token-jev-clean](https://github.com/IAmUnbounded/save-token-jev-clean) - Portable context compaction for coding agents: Jev decides which tool calls still matter, and conversation text stays verbatim. ⭐ 80
- [EliaAlberti/jev-rules](https://github.com/EliaAlberti/jev-rules) - Claude Code plugin where Jev picks which of your rules apply to each prompt, so Claude only sees the relevant ones. ⭐ 64
- [valentynkit/jev-belay](https://github.com/valentynkit/jev-belay) - Claude Code Stop hook that reads the transcript for evidence and, only when files changed with no passing check since, spends one four-question Jev call before letting an unverified "done" stand. ⭐ 21
- [valentynkit/jev.nvim](https://github.com/valentynkit/jev.nvim) - Neovim plugin that asks the buffer a plain-language question, splits it into functions with Treesitter, and ranks Jev's per-function scores in quickfix. ⭐ 8
- [suenot/codex-jev-router](https://github.com/suenot/codex-jev-router) - Chooses Codex subagent model and reasoning effort using Jev Choice and Noul responses, with a Sol fallback. ⭐ 6
- [morcoan/JevSeek](https://github.com/morcoan/JevSeek) - Local coding workspace: Jev routes actions and DeepSeek generates arguments. Native tools, persistent sessions, React desktop app. ⭐ 3
- [ReallyArtificial/jev-by-example](https://github.com/ReallyArtificial/jev-by-example) - Runnable JavaScript lessons using Jev for memory reconciliation, tool-result checks, and handoff decisions, with offline fixtures and opt-in live calls. ⭐ 2

## MCP servers & agent skills

- [jkudish/jev-mcp](https://github.com/jkudish/jev-mcp) - Fast, cheap, typed judgments from Jev as MCP tools. ⭐ 496
- [itsmostafa/typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp) - MCP connector that gives any agent direct access to Jev. ⭐ 339
- [kitze/skillbox](https://github.com/kitze/skillbox) - Self-hosted, versioned skills library for AI agents with optional Jev recommendations. ⭐ 262
- [dbreunig/building-with-jev-skill](https://github.com/dbreunig/building-with-jev-skill) - Agent skill for writing and improving programs that call Jev. ⭐ 151
- [Dicklesworthstone/skillranker](https://github.com/Dicklesworthstone/skillranker) - Rust CLI that ranks agent skills for the next step from live session context. Ships Claude Code hooks. ⭐ 126

## Observability

- [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) - Observability platform with documented Python and TypeScript integrations for tracing TypeSafe System One calls through OpenInference. ⭐ 11.7k
- [Arize-ai/openinference](https://github.com/Arize-ai/openinference) - Python and TypeScript instrumentation that records TypeSafe SDK calls as OpenTelemetry spans with inputs, outputs, model, and token usage. ⭐ 1.2k

## Data, search & classification

- [realZachi/pg-jev](https://github.com/realZachi/pg-jev) - PostgreSQL extension for asking your tables questions in plain language. ⭐ 896
- [superagents-lab/jev-search](https://github.com/superagents-lab/jev-search) - Web search with Jev handling source selection, query understanding, and relevance ranking. ⭐ 512
- [jerryjliu/docjev](https://github.com/jerryjliu/docjev) - Python library, CLI, and local app for document classification and splitting. Uses local LiteParse OCR and hosted Jev decisions, with optional cloud OCR. ⭐ 509
- [kyotofin/tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) - Tax document page classifier. Reports 100% strict accuracy on 261 IRS forms at about $0.001 per page. ⭐ 494
- [robbyczgw-cla/hermes-web-search-plus](https://github.com/robbyczgw-cla/hermes-web-search-plus) - Hermes search plugin with optional Jev checks for news intent, extracted-page quality, and language; disabled by default. ⭐ 419
- [jexp/neo4jev](https://github.com/jexp/neo4jev) - Jev navigates a Neo4j graph by classifying neighbouring relationships. ⭐ 162
- [trungdq88/youtube-sponsor-detection](https://github.com/trungdq88/youtube-sponsor-detection) - Detects YouTube sponsor segments from live audio and transcript. ⭐ 110
- [ChetasLua/jevmeter](https://github.com/ChetasLua/jevmeter) - Scores every sentence of a video with Jev and renders a live meter on a 16:9 edit. ⭐ 107
- [pithings/advocaat](https://github.com/pithings/advocaat) - Small, type-safe client for asking questions about your data with Jev. ⭐ 95
- [giuliosmall/pg_typesafe](https://github.com/giuliosmall/pg_typesafe) - Pre-alpha PostgreSQL extension for categorical classification with Jev. ⭐ 87

## Trading

- [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) - Educational investment research and backtesting with a native Jev adapter for investor decisions. The documented workflow does not place real trades. ⭐ 63.9k
- [jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader) - One buy/sell decision per Monad block on Kuru MON-USDC. Runs in dry-run/mock mode by default and makes no promise of profit. ⭐ 2.8k

> Trading bots can lose money. Read the code and run in dry-run mode first.

## Games & fun

- [rmalde/minecraft-agent](https://github.com/rmalde/minecraft-agent) - Minecraft agent with an LLM planner and Jev selecting bounded Mineflayer actions. Runs against a locally configured server and requires paid model access and machine-specific setup. ⭐ 575
- [fhshaik/typesafe-mario](https://github.com/fhshaik/typesafe-mario) - Jev agent that plays Super Mario Bros. from structured emulator state. ⭐ 433
- [dabit3/jev-experiments](https://github.com/dabit3/jev-experiments) - Assorted Jev experiments. ⭐ 397
- [standardagents/jevpilot](https://github.com/standardagents/jevpilot) - Playable Three.js driving simulator with a Jev-powered autopilot. ⭐ 209
- [valentynkit/jev-plays-pokemon-red](https://github.com/valentynkit/jev-plays-pokemon-red) - Pokemon Red on PyBoy: code owns the route and the arithmetic, Jev picks only at branches, and every battle turn logs a faint prediction scored by Brier against what the RAM says. ⭐ 8

## Apps with Jev inside

Larger products that use Jev for one part of the job.

- [vercel-labs/json-render](https://github.com/vercel-labs/json-render) - Generative UI framework with experimental Jev-based composition from a component catalog. The integration is unreleased and requires a source build. ⭐ 18.5k
- [Asymptote-Labs/agent-beacon](https://github.com/Asymptote-Labs/agent-beacon) - Cross-agent session history and memory. An opt-in command uses Jev to evaluate task success, reusable lessons, and supporting evidence; normal trace capture makes no Jev calls. ⭐ 1.8k
- [anishfn/shapeshift](https://github.com/anishfn/shapeshift) - Text input that selects UI cards using typed Jev intent decisions. Uses a local keyword classifier by default; hosted Jev is optional. ⭐ 816
- [CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy) - Local-first AI office agent. Jev checks each acceptance criterion as a yes/no question in goal mode (README in Chinese). ⭐ 260
- [MillionSend/millionsend](https://github.com/MillionSend/millionsend) - Open-source email platform on AWS SES. The hosted version scores outbound mail with Jev for content monitoring. ⭐ 177

## Community SDKs

Unofficial clients for languages the official SDKs don't cover.

- [cequence-io/openai-scala-client](https://github.com/cequence-io/openai-scala-client) - Scala client with a native TypeSafe System One module for typed questions and a closed-schema adapter for its OpenAI-style interface. ⭐ 255
- [Twister915/typesafe-ai](https://github.com/Twister915/typesafe-ai) - Rust client with async and blocking backends and observable retries. ⭐ 13
- [saibimajdi/typesafeai-dotnet-sdk](https://github.com/saibimajdi/typesafeai-dotnet-sdk) - .NET SDK. ⭐ 12
- [Tangerg/typesafe-sdk-go](https://github.com/Tangerg/typesafe-sdk-go) - Go SDK. ⭐ 9
- [joshmn/typesafe-sdk](https://github.com/joshmn/typesafe-sdk) - Ruby client. ⭐ 7
- [jonesmelton/verdict](https://github.com/jonesmelton/verdict) - OCaml client built on Eio. ⭐ 0

## Open models & replications

None of these are the official TypeSafe model. They are independent projects that copy Jev's input/output shape with open weights.

- [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) - Fine-tuned open decision model, benchmarked against Jev's published numbers. ⭐ 30.8k
- [jaredpalmer/kev](https://github.com/jaredpalmer/kev) - Tiny Jev-like model on Qwen2.5-0.5B that you can train and run on a MacBook. ⭐ 8.5k
- [TheoLeeCJ/SemIf](https://github.com/TheoLeeCJ/SemIf) - "Semantic ifs" from open models on a single home GPU (3090). Formerly `openjev`. ⭐ 4.7k
- [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev) - Nano replica of Jev with parallel decisions, dynamic candidates, and an end-to-end training pipeline. ⭐ 2.5k
- [vinnylarouge/jevlike](https://github.com/vinnylarouge/jevlike) - Trains a Jev-like model on your own data to pick one option from a changing candidate set. More an interesting experiment than a practical tool. ⭐ 1.3k
- [feder-cr/jev](https://github.com/feder-cr/jev) - jevos: independent local yes/no decision model with a Jev-compatible Noul API, served through llama.cpp with CPU support. The jevos binary model does not support Choice or Score questions. ⭐ 1.2k
- [ollaya-dev/ollaya](https://github.com/ollaya-dev/ollaya) - Local runtime for downloading and serving open decision models, including Laya, through a TypeSafe-compatible API. Independent of TypeSafe. ⭐ 1.2k
- [nokia-applied-research/AnyJev](https://github.com/nokia-applied-research/AnyJev) - Independent Jev-style decision library for open models, with Choice, Score, and Noul questions, logit readouts, and optional learned heads. ⭐ 1k
- [Rizzo-AI-Academy/rizzo-flow](https://github.com/Rizzo-AI-Academy/rizzo-flow) - Independent local decision server that scores open-model logits for Choice, Score, and Noul questions, with a TypeSafe-compatible System One endpoint. ⭐ 824
- [receptron/laya](https://github.com/receptron/laya) - Node.js/TypeScript runtime for the independent Laya model using ONNX, exposing Jev-shaped typed questions and answers locally. ⭐ 785
- [featherless-ai/simple-jev](https://github.com/featherless-ai/simple-jev) - Turns any open model into a classifier / Jev-style endpoint. ⭐ 586
- [ekzhang/openjev-sglang](https://github.com/ekzhang/openjev-sglang) - Jev-compatible, prefill-only API endpoint built on open models with SGLang. ⭐ 336
- [hr98w/jev-visual](https://github.com/hr98w/jev-visual) - Educational Jev-like visual inference experiment on Apple Silicon. ⭐ 306
- [kshetrajna12/reflex](https://github.com/kshetrajna12/reflex) - Small open decision model on Qwen3.5: state plus typed questions in, calibrated probabilities out. ⭐ 162
- [iammrduncan/typesafe-ai-benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark) - LLM gateway that imitates TypeSafe's structured output, for benchmarking against the real thing. ⭐ 38
- [SamratDuttaOfficial/WaterSheep](https://github.com/SamratDuttaOfficial/WaterSheep) - Independent open-weight decision model fine-tuned from ModernBERT-base that answers Noul, Choice, Score and multi-label questions with a probability per option, through a TypeSafe-compatible `/v1/systemone` server or in the browser with ONNX. ⭐ 6

## Other lists

- [yibie/awesome-jev](https://github.com/yibie/awesome-jev) - Public projects, integrations, and discussions. ⭐ 2.1k
- [Anil-matcha/awesome-jev-by-typesafe](https://github.com/Anil-matcha/awesome-jev-by-typesafe) - Use cases, patterns, prompts, and starter code. ⭐ 899
- [AnotiaWang/awesome-jev](https://github.com/AnotiaWang/awesome-jev) - Applications, libraries, and resources for Jev and System One. ⭐ 608
- [AbdelStark/awesome-typesafe](https://github.com/AbdelStark/awesome-typesafe) - Official resources and community projects for TypeSafe and System One models. ⭐ 562
- [cobanov/awesome-jev](https://github.com/cobanov/awesome-jev) - Source-backed list of projects built with Jev. ⭐ 506
- [fatwang2/awesome-jev](https://github.com/fatwang2/awesome-jev) - Project directory plus a reusable Jev-based GitHub review workflow. ⭐ 220
- [kraayenjon/awesome-jev](https://github.com/kraayenjon/awesome-jev) - Curated list of Jev use cases, projects, SDKs and resources, kept alongside madewithjev.com.

## Contributing

Found something good? Open a pull request. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

This list is released under [CC0 1.0](LICENSE). This project is not affiliated with TypeSafe AI.
