# 🔬 EXPERIMENT 13: Integrating JUnit with Jenkins

---

## 🎯 AIM

To integrate JUnit testing with Jenkins and execute test cases using Continuous Integration.

---

## 🧠 THEORY

* **Jenkins** is an automation server used for CI/CD.
* It automates build, test, and deployment processes.
* Integration with JUnit enables automated testing and report generation.

---

## 🛠️ TOOLS REQUIRED

* Java JDK (11 or above)
* Maven (3.9+)
* Jenkins (installed and running)
* Existing Maven project (junit-demo)

---

## ⚙️ STEP 1: START JENKINS

Open browser:

```text
http://localhost:8080
```

Login with admin credentials.

---

## ⚙️ STEP 2: INSTALL REQUIRED PLUGINS

Go to:
👉 Manage Jenkins (⚙️ icon) → Plugins

Install:

* Maven Integration Plugin
* JUnit Plugin
* Git Plugin

Restart Jenkins if required.

---

## ⚙️ STEP 3: CONFIGURE TOOLS

Go to:
👉 Manage Jenkins → Global Tool Configuration

### Add JDK:

* Name: JDK11
* Select: Install automatically

### Add Maven:

* Name: Maven3
* Select: Install automatically

Click Save.

---

## 📁 STEP 4: CREATE NEW JOB

* Click **New Item**
* Name: `JUnit-Test-Job`
* Select: **Freestyle Project**
* Click OK

---

## ⚙️ STEP 5: CONFIGURE JOB

### 🔹 General Section

Click **Advanced** → Enable:

```text
✔ Use custom workspace
```

Enter project path:

```text
C:\Users\danis\OneDrive\Pictures\Documents\devopslab\junit-demo
```

---

### 🔹 Build Section

Add:

👉 **Invoke top-level Maven targets**

Fill:

```text
Maven Version: Maven3
Goals: clean test
```

---

### 🔹 Post-Build Action

Add:

👉 **Publish JUnit test result report**

Enter:

```text
target/surefire-reports/*.xml
```

---

## ▶️ STEP 6: BUILD PROJECT

Click:

```text
Build Now
```

---

## ▶️ STEP 7: VIEW OUTPUT

* Click Build number → Console Output

### Expected:

```text
BUILD SUCCESS
Tests run: 3, Failures: 0
```

---

## ▶️ STEP 8: VIEW TEST REPORT

* Click **Test Result**

Displays:

* Total tests
* Passed tests
* No failures

---

## 📊 RESULT

* Jenkins successfully executed Maven build
* JUnit tests were run automatically
* Test reports were generated and displayed

---

## 🧠 VIVA QUESTIONS

1. What is Jenkins?
   → Automation server for CI/CD

2. What is CI?
   → Continuous Integration

3. What is Freestyle project?
   → Basic Jenkins job configuration

4. What is Maven in Jenkins?
   → Used to build and run tests

5. What is JUnit report?
   → XML report of test results

6. Why custom workspace is used?
   → To point Jenkins to local project

---

## ⚠️ COMMON ERRORS

* Missing pom.xml in workspace
* Wrong project path
* Missing plugins
* Incorrect test report path
* Multiple build steps

---

## ✅ CONCLUSION

Integration of JUnit with Jenkins enables automated testing, improves code quality, and forms the foundation of CI/CD pipelines.

---
