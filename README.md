# IDS 706 Data Engineering Individual Project # 1
[![Format](https://github.com/nogibjj/Individual_PJT_1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Individual_PJT_1/actions/workflows/format.yml)
[![Install](https://github.com/nogibjj/Individual_PJT_1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Individual_PJT_1/actions/workflows/install.yml)
[![Lint](https://github.com/nogibjj/Individual_PJT_1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Individual_PJT_1/actions/workflows/lint.yml)
[![Test](https://github.com/nogibjj/Individual_PJT_1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Individual_PJT_1/actions/workflows/test.yml)

***
## Summary
This project demonstrates how continuous integration (CI) in Python-based data science projects could be implemented with GitHub Actions. The workflows encompass tasks such as code listing, formatting, dependency installation, and test execution. Essential procedures are therefore automatically triggered with each repository push and pull request, streamlining the development process. The primary benefit of using CI is that we can ensure overall code quality and consistency during the whole development process. Plus, these processes can be automated in the GitHub environment. 
***

## Key components in the repository are:

  1. **Jupyter Notebook**: contains cells that perform descriptive statistical analysis using the Pandas library. 
  2. **Python Script**: provides a script-based approach to executing the same descriptive statistical analysis using the Pandas library. 
  3. **Shared Code (lib.py)**: contains reusable code modules shared between the Jupyter Notebook and Python script, facilitating code organization and maintainability. 
  4. **Makefile**: specifies essential commands executed by GitHub Workflows for every push and pull request:
      * Test: executes all available tests including those for Jupyter notebook, script, and library.
      * Format: formats code with Python black formatter 
      * Lint: lints the code with Ruff  
      * Install: runs and loads external packages and libraries indicated in my requirements.txt using "pip install -r requirements.txt" command.  
  5. **Test_script.py and Test_lib.py**: contains test cases specifically designed to guarantee the code's functionality and validity 
  7. **Pinned requirements.txt**: lists specific versions of project dependencies to ensure consistency across a variety of environments.
  8. **GitHub Actions**: includes cicd.yml file which automatically setup the CI process. Github Action will be started by every push or merge is done.  
***

## Github Actions
A successful run will look like the following screenshot. 

![image](https://github.com/nogibjj/Individual_PJT_1/assets/141780408/0e8d0fc7-5ed6-4c4e-877c-7dbf5a0dff45)

*** 

## Descriptive Statistics & Data Visualization 
### 1. Summary Statistics 
![image](https://github.com/nogibjj/Individual_PJT_1/assets/141780408/cf132793-8d7e-48d3-a6ef-f4979ad96f1b)

### 2. Scatter Plot
![image](https://github.com/nogibjj/Individual_PJT_1/assets/141780408/70572614-9adb-47c6-8553-6f48d0f8d689)

### 3. Box Plot
![image](https://github.com/nogibjj/Individual_PJT_1/assets/141780408/250a502a-6927-454b-8753-616805805f79)

### 4. Pie Chart
![image](https://github.com/nogibjj/Individual_PJT_1/assets/141780408/255469a4-c425-4185-8b90-ce93d6e8bdd5)


