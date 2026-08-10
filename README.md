# platform-api-first-query

[365.altium.com]: https://365.altium.com/

A collection of example applications that illustrate an API-first approach to
querying the [Altium 365][365.altium.com] platform through its GraphQL API.

The examples are provided per language. In each language, a "Hello Workspace"
example gets you started, along with a number of use cases that query the
platform in different ways — see the language-specific README for the current list.

## Prerequisites

These apply regardless of the language you use:

- [Altium 365][365.altium.com] credentials
- Administrator access to a A365 workspace.
- A token created for that A365 workspace in Admin -> Developer.

When you create a new token, you choose how to authenticate:

- Generate a Personal Access Token (PAT) — the default, with the Refresh Token
  option left unchecked, or
- Generate a refresh token by ticking the Refresh Token option. This also gives you
  a Client ID and Client Secret.

## Providing credentials

The examples read your credentials from local variables that you paste directly
into the example source. Depending on the authentication option you chose above,
fill in either:

- `PAT`, or
- `CLIENT_ID`, `CLIENT_SECRET` and `REFRESH_TOKEN`.

See the language-specific README for the exact file and variables.

## Examples by language

### Python

See [python/README.md](python/README.md).

- **Hello Workspace** — a basic example that reads metadata from your Altium 365 workspace.
