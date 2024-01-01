## Running the Test Page (sample_page):

`npm install -g http-server`

then in the sample_page folder:

`http-server`

### In case of "...http-server.ps1 cannot be loaded because running scripts is disabled on this system."

you should execute the following command in the PowerShell console in administrator mode:

`Set-ExecutionPolicy Unrestricted`

then, after finishing your work, you should restore the previous settings with the command:

`Set-ExecutionPolicy Restricted`

to check the current policy:

`Get-ExecutionPolicy`

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

## xss_tester.py

Module Selenium is required. Installation command:

`pip install selenium`

To run xss_tester.py:

`python xss_tester.py`
