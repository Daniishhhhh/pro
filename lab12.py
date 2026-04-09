# 🔬 EXPERIMENT 12: Running JUnit Tests with Maven

---

## 🎯 AIM

To configure Maven and execute JUnit test cases using Maven build tool.

---

## 🧠 THEORY

* **Maven** is a build automation tool used for managing dependencies and project lifecycle.
* It automatically compiles code, runs tests, and builds the project using predefined phases.

---

## 🛠️ TOOLS REQUIRED

* Java JDK (11 or above)
* Maven (3.9+)
* IDE (IntelliJ / Eclipse)
* JUnit dependency

---

## 📁 STEP 1: USE EXISTING PROJECT

Navigate to previously created project:

```bash
cd junit-demo
```

---

## 📁 PROJECT STRUCTURE

```text
junit-demo/
 ├── pom.xml
 └── src/
     ├── main/java/com/devops/Calculator.java
     └── test/java/com/devops/CalculatorTest.java
```

---

## ⚙️ STEP 2: VERIFY pom.xml

Ensure JUnit dependency is present:

```xml
<dependencies>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter</artifactId>
        <version>5.10.0</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```

---

## ⚙️ STEP 3: ADD MAVEN SUREFIRE PLUGIN (OPTIONAL BUT RECOMMENDED)

Add inside `<build>` section in `pom.xml`:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>3.1.2</version>
        </plugin>
    </plugins>
</build>
```

---

## ▶️ STEP 4: COMPILE PROJECT

```bash
mvn compile
```

### ✅ Expected:

* Code compiles successfully
* No errors

---

## ▶️ STEP 5: RUN TESTS USING MAVEN

```bash
mvn test
```

---

## 🔄 MAVEN BUILD LIFECYCLE (IMPORTANT)

```text
validate → compile → test → package → verify → install → deploy
```

* `compile` → compiles source code
* `test` → runs JUnit test cases
* `package` → creates JAR file

---

## ▶️ STEP 6: PACKAGE PROJECT

```bash
mvn package
```

### ✅ Output:

```text
target/junit-demo-1.0-SNAPSHOT.jar
```

---

## ▶️ STEP 7: CLEAN PROJECT

```bash
mvn clean
```

* Deletes `target` folder
* Removes compiled files

---

## ▶️ STEP 8: FULL BUILD

```bash
mvn clean install
```

* Cleans project
* Compiles code
* Runs tests
* Installs JAR into local repository

---

## ✅ EXPECTED OUTPUT

```text
BUILD SUCCESS
Tests run: 3, Failures: 0, Errors: 0
```

---

## 📊 RESULT

* Maven successfully compiled the project
* JUnit tests executed using Maven
* Build lifecycle understood
* Project packaged into JAR file

---

Maven simplifies build and testing process by automating compilation, dependency management, and execution of test cases.

---
