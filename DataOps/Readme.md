1. create and activate a python virtual environment.
virtualenv api_project
source api_project/bin/activate

2. Install the requirements
pip install -r requirements.txt

.
.
Installing collected packages: text-unidecode, pytz, coolname, zipp, websockets, urllib3, ujson, tzlocal, tzdata, typing-extensions, toml, threadpoolctl, sniffio, six, shellingham, ruamel.yaml.clib, rpds-py, regex, readchar, pyyaml, python-slugify, python-dotenv, pyparsing, pygments, pycparser, prometheus-client, pillow, pathspec, packaging, orjson, oauthlib, numpy, mdurl, MarkupSafe, kiwisolver, jsonpointer, joblib, idna, hyperframe, humanize, hpack, h11, greenlet, graphviz, fsspec, fonttools, exceptiongroup, cycler, colorama, cloudpickle, click, charset-normalizer, certifi, cachetools, attrs, async-timeout, annotated-types, uvicorn, sqlalchemy, scipy, ruamel.yaml, rfc3339-validator, requests, referencing, python-dateutil, pydantic-core, markdown-it-py, Mako, jsonpatch, jinja2, importlib-resources, importlib-metadata, httpcore, h2, griffe, contourpy, cffi, asyncpg, asgi-lifespan, anyio, aiosqlite, time-machine, starlette, scikit-learn, rich, requests-oauthlib, pydantic, pandas, matplotlib, markdown, jsonschema-specifications, jinja2-humanize-extension, httpx, docker, dateparser, cryptography, croniter, alembic, typer, seaborn, pydantic-settings, pydantic-extra-types, pendulum, jsonschema, fastapi, apprise, prefect
.
.
Successfully installed Mako-1.3.5 MarkupSafe-2.1.5 aiosqlite-0.20.0 alembic-1.13.3 annotated-types-0.7.0 anyio-4.6.0 apprise-1.9.0 asgi-lifespan-2.1.0 async-timeout-4.0.3 asyncpg-0.29.0 attrs-24.2.0 cachetools-5.5.0 certifi-2024.8.30 cffi-1.17.1 charset-normalizer-3.3.2 click-8.1.7 cloudpickle-3.0.0 colorama-0.4.6 contourpy-1.3.0 coolname-2.2.0 croniter-3.0.3 cryptography-43.0.1 cycler-0.12.1 dateparser-1.2.0 docker-7.1.0 exceptiongroup-1.2.2 fastapi-0.115.0 fonttools-4.54.1 fsspec-2024.9.0 graphviz-0.20.3 greenlet-3.1.1 griffe-1.3.1 h11-0.14.0 h2-4.1.0 hpack-4.0.0 httpcore-1.0.5 httpx-0.27.2 humanize-4.10.0 hyperframe-6.0.1 idna-3.10 importlib-metadata-8.5.0 importlib-resources-6.4.5 jinja2-3.1.4 jinja2-humanize-extension-0.4.0 joblib-1.4.2 jsonpatch-1.33 jsonpointer-3.0.0 jsonschema-4.23.0 jsonschema-specifications-2023.12.1 kiwisolver-1.4.7 markdown-3.7 markdown-it-py-3.0.0 matplotlib-3.9.2 mdurl-0.1.2 numpy-2.0.2 oauthlib-3.2.2 orjson-3.10.7 packaging-24.1 pandas-2.2.3 pathspec-0.12.1 pendulum-3.0.0 pillow-10.4.0 prefect-3.0.3 prometheus-client-0.21.0 pycparser-2.22 pydantic-2.9.2 pydantic-core-2.23.4 pydantic-extra-types-2.9.0 pydantic-settings-2.5.2 pygments-2.18.0 pyparsing-3.1.4 python-dateutil-2.9.0.post0 python-dotenv-1.0.1 python-slugify-8.0.4 pytz-2024.2 pyyaml-6.0.2 readchar-4.2.0 referencing-0.35.1 regex-2024.9.11 requests-2.32.3 requests-oauthlib-2.0.0 rfc3339-validator-0.1.4 rich-13.8.1 rpds-py-0.20.0 ruamel.yaml-0.18.6 ruamel.yaml.clib-0.2.8 scikit-learn-1.5.2 scipy-1.13.1 seaborn-0.13.2 shellingham-1.5.4 six-1.16.0 sniffio-1.3.1 sqlalchemy-2.0.35 starlette-0.38.6 text-unidecode-1.3 threadpoolctl-3.5.0 time-machine-2.15.0 toml-0.10.2 typer-0.12.5 typing-extensions-4.12.2 tzdata-2024.2 tzlocal-5.2 ujson-5.10.0 urllib3-2.2.3 uvicorn-0.31.0 websockets-13.1 zipp-3.20.2

3. Run basic stats
cd tasks/
python BasicStats.py

4. Run EDA
cd tasks/
python PearsonCorrelation.py
python Binning.py

5. PREFECT

API_KEY=pnu_4t3M9YNXs6TytZ5PNmzIM2gcicvXQL16BZBG 
ACCOUNT_ID=ea639eed-d04f-46a7-ae65-4576fa087022
WORKSPACE_ID=e15c14f8-cea0-41dc-bd42-d4b2899de804


(api_project) adimulamramkumar-mac:tasks adimulamramkumar$ prefect cloud login -k pnu_4t3M9YNXs6TytZ5PNmzIM2gcicvXQL16BZBG 
Authenticated with Prefect Cloud! Using workspace 'bitspilani-wilp/default'.
(api_project) adimulamramkumar-mac:tasks adimulamramkumar$ 

(api_project) adimulamramkumar-mac:tasks adimulamramkumar$ prefect cloud workspace ls
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Workspaces:               ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ * bitspilani-wilp/default │
└───────────────────────────┘
     * active workspace      
(api_project) adimulamramkumar-mac:tasks adimulamramkumar$ 

(api_project) adimulamramkumar-mac:tasks adimulamramkumar$ prefect cloud workspace set --workspace bitspilani-wilp/default 
Successfully set workspace to 'bitspilani-wilp/default' in profile 'local'.
(api_project) adimulamramkumar-mac:tasks adimulamramkumar$ 

(api_project) adimulamramkumar-mac:flows adimulamramkumar$ python workflow.py 
Your flow 'main-flow' is being served and polling for scheduled runs!

To trigger a run for this flow, use the following command:

        $ prefect deployment run 'main-flow/heart-attack-risk-workflow'

You can also run your flow via the Prefect UI: https://app.prefect.cloud/account/447374eb-6251-4bfb-b0c7-18f7c4be91d0/workspace/e15c14f8-cea0-41dc-bd42-d4b2899de804/deployments/deployment/d5267dcf-f84e-4120-8334-c1e770169c7e

..

Another terminal:

(api_project) adimulamramkumar-mac:Code adimulamramkumar$ prefect deployment run 'main-flow/heart-attack-risk-workflow'
Creating flow run for deployment 'main-flow/heart-attack-risk-workflow'...
Created flow run 'illustrious-rhino'.
└── UUID: e632ebcd-5bff-4f50-867b-77dd12a40346
└── Parameters: {}
└── Job Variables: {}
└── Scheduled start time: 2024-09-28 22:01:19 IST (now)
└── URL: https://app.prefect.cloud/account/447374eb-6251-4bfb-b0c7-18f7c4be91d0/workspace/e15c14f8-cea0-41dc-bd42-d4b2899de804/runs/flow-run/e632ebcd-5bff-4f50-867b-77dd12a40346
(api_project) adimulamramkumar-mac:Code adimulamramkumar$ 


Check Prefect dashboard.
