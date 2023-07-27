# Welcome to DevSecOps/Engineering assessment

Hello! Welcome to this assessment, in this challenge, we'll provide an application, and we'd like you to propose and implement the best solution for its deployment.

### **We'd like to see your work and coding skills, so please provide your own repo with the proposed solution**

The application depends on:
- A Client Side Render Frontend [repo here](https://github.com/4k4xs4pH1r3/DevSecOps/tree/master/Frontend)
- A Backend service [repo here](https://github.com/4k4xs4pH1r3/DevSecOps/tree/master/Backend)

Both applications run as they are, but you are free to modify them as you see fit for the solution you wish to propose.

# Evaluation rules
- We expect the following:
    - Use infrastructure as code IaC, a container-based solution that would implement the necessary resources for this app to work; AWS oriented is preferred but not mandatory.
    - CI/CD pipeline proposition, Using the last version of each component ever instead of pinning a specific version when possible.
- Your solution must scale and be highly secure, clearing the alerts in Security Tab.
- Meaningful git commits; we'd like to see how you got to the final solution presented by sending the PRs to this repo.
- Update the README file with information on the solution and how to operate it.

# Extra points for:
- a fully working hosted version of your solution
- Horizontal auto-scaling solution proposition
- How would you make sure this application won't fail during high loads and/or traffic?
- How would you design your solution for zero-downtime deployment and scale?
- Feedback on the applications given.

Best of Luck!
