# platform-api-first-query — Python examples

Simple console apps which illustrate a number of queries in Altium 365:
- Hello Workspace basic example that gets metadata from your Altium 365 workspace
- A number of use cases (under `UseCases/`), such as looking up project revisions
  and parameters, or checking library component compliance, from your Altium 365
  workspace.

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

## Use cases

Each use case lives under `UseCases/` in its own folder. Before running any of
them, open the use case's Python file and paste your credentials into the
variables near the top of the file. Depending on the authentication option you
chose, fill in either:
- `PAT`, or
- `CLIENT_ID`, `CLIENT_SECRET` and `REFRESH_TOKEN`.

See [Providing credentials](../README.md#providing-credentials) in the root README
for background on the two options.

### Project revisions and parameters use case

Open `UseCases/ProjectRevisionsAndReleases/project_revisions_and_parameters.py`,
fill in your credentials as described above, then run it:

```bash
python UseCases/ProjectRevisionsAndReleases/project_revisions_and_parameters.py
```

### Library compliance use case

Open `UseCases/LibraryCompliance/library_compliance.py` and fill in your
credentials as described above.

The script walks the component library of each accessible workspace, extracts the
compliance parameters (RoHS, REACH, ...) from every component, and highlights in
red those that are **not** RoHS compliant, ending with a summary of the offending
components.

Then run it:

```bash
python UseCases/LibraryCompliance/library_compliance.py
```

### Overriding default endpoints
Default endpoints are provided for A365 GraphQL API and Refresh Token.
Those can be overridden if needed by setting the following environment variables:
- `A365_URL` for A365 GraphQL API endpoint override
- `TOKEN_URL` for Refresh Token endpoint override
