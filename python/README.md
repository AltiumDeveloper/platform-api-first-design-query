# platform-api-first-query — Python examples

Simple console apps which illustrate a number of queries in Altium 365:
- Hello Workspace basic example that gets metadata from your Altium 365 workspace
- A number of use cases (under `UseCases/`), such as looking up project revisions
  and parameters from your Altium 365 workspace.

See the [root README](../README.md) for prerequisites and how to get your
Altium 365 token. This README covers running the Python examples once you
have your credentials.

## Setup

From the `python/` directory, create and activate a virtual environment and
install the dependencies.

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If PowerShell blocks the activation script with an execution-policy error, allow
it for the current session only and try again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

**Windows (Command Prompt):**

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

Once the environment is activated, your prompt is prefixed with `(.venv)` and the
`python` command below refers to the virtual environment's interpreter.

## Hello Workspace

From your A365 workspace -> Admin -> Developer:
- Generate a Personal Access Token (PAT) — the default, with the Refresh Token
  option left unchecked
- Paste that into the `PAT` variable in `hello_workspace.py`
- Make sure you point `WORKSPACE_URL` to your workspace

Then run it:

```bash
python hello_workspace.py
```

## Project revisions and parameters use case

Open `UseCases/ProjectRevisionsAndReleases/project_revisions_and_parameters.py`
and paste your credentials into the variables near the top of the file. Depending
on the authentication option you chose, fill in either:
- `PAT`, or
- `CLIENT_ID`, `CLIENT_SECRET` and `REFRESH_TOKEN`.

See [Providing credentials](../README.md#providing-credentials) in the root README
for background on the two options.

Then run it:

```bash
python UseCases/ProjectRevisionsAndReleases/project_revisions_and_parameters.py
```

### Overriding default endpoints
Default endpoints are provided for A365 GraphQL API and Refresh Token.
Those can be overridden if needed by setting the following environment variables:
- `A365_URL` for A365 GraphQL API endpoint override
- `TOKEN_URL` for Refresh Token endpoint override
