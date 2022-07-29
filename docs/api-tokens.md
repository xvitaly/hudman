# API tokens

## About API tokens

This library uses API tokens from following third-party services:

  * GitHub.

## Getting API tokens

In order to use this application in authorized mode, you need to receive the following API tokens:

* [GitHub API personal access token](https://docs.github.com/en/articles/creating-a-personal-access-token-for-the-command-line).

## Forwarding API tokens to application

Application need both GitHub user name and API token, forwarded as environment variables:

  * `HUDMAN_LOGIN` - GitHub user login;
  * `HUDMAN_APIKEY` - GitHub API personal access token.
