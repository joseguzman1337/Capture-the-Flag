# Welcome to Capture the Flag DevSecOps/Engineering challenge

[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/0/badge)](https://bestpractices.coreinfrastructure.org/projects/0)
[![OpenSSF Scorecard](https://img.shields.io/ossf-scorecard/github.com/joseguzman1337/Capture-the-Flag?label=openssf%20scorecard&style=flat)](https://scorecard.dev/viewer/?uri=github.com/joseguzman1337/Capture-the-Flag)
[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](LICENSE)
[![CodeQL](https://github.com/joseguzman1337/Capture-the-Flag/actions/workflows/codeql.yml/badge.svg)](.github/workflows/codeql.yml)
[![Scorecard](https://github.com/joseguzman1337/Capture-the-Flag/actions/workflows/scorecard.yml/badge.svg)](.github/workflows/scorecard.yml)
[![Backend tests](https://github.com/joseguzman1337/Capture-the-Flag/actions/workflows/backend-tests.yml/badge.svg)](.github/workflows/backend-tests.yml)
[![Frontend build](https://github.com/joseguzman1337/Capture-the-Flag/actions/workflows/frontend-tests.yml/badge.svg)](.github/workflows/frontend-tests.yml)
[![pip-audit](https://github.com/joseguzman1337/Capture-the-Flag/actions/workflows/pip-audit.yml/badge.svg)](.github/workflows/pip-audit.yml)
[![Dependabot](https://img.shields.io/badge/Dependabot-enabled-025e8c?logo=dependabot)](.github/dependabot.yml)

Welcome, in this challenge, we'll provide an application, and we'd like you to propose and implement the best solution for its secure deployment.

**We'd like to see your work experience and secure coding skills to find flags, so please update this repo with your proposed solution.**

The application depends on:

- A Client Side Render Frontend [repo here](https://github.com/4k4xs4pH1r3/DevSecOps/tree/master/Frontend)
- A Backend service [repo here](https://github.com/4k4xs4pH1r3/DevSecOps/tree/master/Backend)

## Evaluation rules

Expectations and Objectives:

- Both applications should run a fully working hosted version of your DevSecOps solution. But you are free to modify them as you see fit for the solution you wish to propose.
- Use infrastructure as code IaC, a container-based solution that would implement the necessary resources for this app to work; AWS oriented is preferred but not mandatory.
- Add all the missing GitHub Workflows, fix the existing ones, and add to each one their badges inside of this README file to identify the smell of Your code.
- CI/CD pipeline proposition, using the last version of each component ever instead of pinning a specific version when possible.
- Meaningful git commits; we'd like to see how you got to the final solution presented by sending the PRs to this repo.
- Your solution must scale and be highly secure, clearing all the alerts in Security Tab.
- Update the README file with information on the solution and how to operate it.
- Create the Release and the Package.

## Extra points for

- Create a Cyber Security architecture diagram in draw.io and add the google drive link to it here.
- How would you make sure this application won't fail during high loads and/or traffic?
- How would you design your solution for zero-downtime deployment and scale?
- Horizontal auto-scaling solution proposition.
- Feedback on the applications given.

Best of Luck!
