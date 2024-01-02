# XSS Demo Site and Testing Tool

## Step-by-step instructions:

### 1. Running the Test Page (sample_page):

`npm install -g http-server`

Then, navigate to the vulnerable_page folder and run:

`http-server`

If the server starts without issues, the testing page is ready to go.

---

### In case of "...http-server.ps1 cannot be loaded because running scripts is disabled on this system.":

Execute the following command in the PowerShell console with administrator privileges:

`Set-ExecutionPolicy Unrestricted`

After finishing your work, you should restore the previous settings with the command:

`Set-ExecutionPolicy Restricted`

To check the current policy, use:

`Get-ExecutionPolicy`

---

### 2. Running the Testing Tool - xss_tester.py

The Selenium module is required. To install it, use the following command:

`pip install selenium`

After installing Selenium, run xss_tester.py:

`python xss_tester.py`

This application tests the Sample Page for XSS vulnerabilities and displays the information in the console.

**You can also test the application's functionality using the example of a page secured against XSS attacks, which is located in the vulnerable_page folder.**

---

## XSS Vulnerability Testing Scripts

Two simple JavaScript snippets used for testing the susceptibility of a web application to Cross-Site Scripting (XSS) attacks.

### 1. Basic Alert Script

```html
<script>
  alert("XSS");
</script>
```

### 2. Cookie Theft Script

```html
<script>
  if (document.cookie) {
    alert("Available cookies: " + document.cookie);
  } else {
    alert("No cookies available.");
  }
</script>
```
