# Challenge Exercises

Now you've had an opportunity to get started using GitHub Copilot, we have a number of challenges for you to attempt. Remember the goal here is not to test your programming abilities but rather, see how you can use GitHub Copilot to help you complete these tasks. Even if you've never programmed in Python, you may be surprised how Copilot can help you be successful with these challenge.



<details>
<summary>Challenge #1 - Refining your Terraform file with Copilot assistance</summary>

### Refining your Terraform file with Copilot assistance

Try to improve the code suggested by Copilot by yourself. For example, try to change the following:
- Change the size of Azure VM
- Change the OS of the Azure VM
- Change the network interface of Azure VM to another one
This will allow you to see how your favourite AI Pair programmer can help you to refine your code by providing helpful suggestions. This should mean less time consuming trial and error and more time to focus on the task at hand.

</details>

<details>
<summary>Challenge #2 - Document your terraform file</summary>

### Document your terraform file

Try writing documentation for this Terraform script; GitHub Copilot will make suggestions for natural language documentation as well.

</details>

<details>
<summary>Challenge #3 - Creating a new terraform file</summary>

### Creating a new terraform file

Try creating a new file and writing a Terraform script and see what suggestions GitHub Copilot makes. You will probably find that on a completely new file, GitHub Copilot's suggestions are often not exactly what you intended. At that point, you may want to write some resource definitions yourself, or write detailed comments.

</details>


<details>
<summary>Challenge #4 - Verify your Terraform file using tfsec</summary>

### Verify your Terraform file using tfsec

- `tfsec` is an open source static analysis security scanner for your Terraform code. Use `tfsec` to verify that the terraform file you've just completed to detect any issues.
>:bulb: tfsec is preinstalled in the Codespaces environment. If you are not using the Codespaces environment, you will need to visit https://aquasecurity.github.io/tfsec/v1.28.1/ to install the tool locally.
- In VSCode, in the **terminal** panel, enter `tfsec` to run the tool against the terraform file. Depending on any changes you've made, there will likely be a number of issues identified. It's important to realise that GitHub Copilot's output (or any generated output for that matter) should always be reviewed and verified. Your existing processes should be followed to ensure that any changes are reviewed and approved before being merged into your main branch.
</details>
