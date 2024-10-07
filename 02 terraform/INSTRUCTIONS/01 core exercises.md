## Workshop exercises

### Core exercise


<summary>1a. Defining resources in a Terraform file</summary>

### Step by step instructions


:bulb:  When you see the :leftwards_arrow_with_hook: symbol, you need to press the ENTER key.


1. After completing the steps detailed in [1. setup.md](<./1. setup.md>), you should have either VScode (or a supported IDE) open **OR** a GitHub Codespace open in your browser. If you have neither, please complete the steps in [1. setup.md](<./1. setup.md>) before continuing.

2. Ensure you can see the files in the **Explorer view**. If not, click the **Explorer View icon** on the left sidebar of your editor.

<img width="398" alt="Code Explorer View" src="../assets/Code Explorer View.png">

3. Double click on the `variables.tf` file in the Explorer view. This file defines the inputs required to deploy an Azure VM. We won't be editing this file. 
> :bulb: Simply by having this file open in a tab, it will provide additional context to GitHub Copilot to enhance the suggestions Copilot will present.

4. Double click on the `main.tf` file in the Explorer view. This is the Terraform script we are going to edit. We've already defined some resources like a resource group and a virtual network. We're going to add a few additional resources with the help of GitHub Copilot such as a security group and finally a virtual machine.

<img width="692" alt="Open in a Codespace" src="../assets/Variables and main files open.png">

5. Let's add a Security Group resource to our Terraform file. Navigate to the end of the main.tf file and add the following comment.

```// Security Group```  :leftwards_arrow_with_hook:

6. Copilot should now suggest the code block to use for a Security Group. Once it appears, press **TAB** then **ENTER** to accept the suggestion.
> :bulb: Remember: GitHub Copilot is a pair programmer. It is the human's responsibility to review the suggestions and accept the ones that make sense.

<img width="618" alt="Code Explorer View" src="../assets/Copilot - Security Group Suggestion.png">

7. Next, let's associate our new security group with the existing network interfaces defined earlier in the Terraform file. At the end of the `main.tf` file, add the following comment.

```// Main network interface security group association```  :leftwards_arrow_with_hook:

8. Copilot should now suggest the code block to use to assocaite the new security group with the existing network interfaces. Once it appears, press **TAB** then **ENTER** to accept the suggestion.

<img width="611" alt="Code Explorer View" src="../assets/Copilot - Network Suggestion.png">

9. Finally, let's define an Azure VM resource. At the end of the `main.tf` file, add the following comment.

```// Virtual Machine```   :leftwards_arrow_with_hook:

10. Copilot should now suggest the code block to use to create a Virtual Machine. Once it appears, press **TAB** then **ENTER** to accept the suggestion. Notice how the suggested code block references resources defined previously.



You're now ready to start the [challenge exercises](<./3. challenge exercises.md>) to see how you can leverage the power of GitHub Copilot to solve a number of challenges yourself.

