# 🔬 EXPERIMENT 11: Writing Unit Tests using JUnit

---

## 🎯 AIM

To write a Java program and test it using JUnit framework.

---

## 🧠 THEORY

* **JUnit** is a testing framework used to test Java applications automatically.
* It uses **test cases and assertions** to verify correctness of code.

---

## 🛠️ TOOLS REQUIRED

* Java JDK (11 or above)
* Maven (3.9+)
* IDE (IntelliJ / Eclipse)

---

## 📁 STEP 1: CREATE MAVEN PROJECT

Run the following command in terminal:

```bash
mvn archetype:generate -DgroupId=com.devops -DartifactId=junit-demo -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
```

---

## 📁 STEP 2: NAVIGATE TO PROJECT

```bash
cd junit-demo
```

---

## 📁 PROJECT STRUCTURE

```
junit-demo/
 ├── pom.xml
 └── src/
     ├── main/java/com/devops/
     └── test/java/com/devops/
```

---

## ⚙️ STEP 3: MODIFY pom.xml

Replace the `<dependencies>` section with:

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

## 🧹 STEP 4: REMOVE DEFAULT FILES

Delete the following files:

```
src/main/java/com/devops/App.java
src/test/java/com/devops/AppTest.java
```

---

## 💻 STEP 5: CREATE JAVA PROGRAM

### 📄 File: Calculator.java

📁 Location: `src/main/java/com/devops/`

```java
package com.devops;

public class Calculator {

    public int add(int a, int b) {
        return a + b;
    }

    public int divide(int a, int b) {
        if (b == 0) {
            throw new ArithmeticException("Cannot divide by zero");
        }
        return a / b;
    }
}
```

---

## 🧪 STEP 6: CREATE JUNIT TEST CASES

### 📄 File: CalculatorTest.java

📁 Location: `src/test/java/com/devops/`

```java
package com.devops;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class CalculatorTest {

    Calculator calc = new Calculator();

    @Test
    public void testAdd() {
        assertEquals(5, calc.add(2, 3));
    }

    @Test
    public void testDivide() {
        assertEquals(2, calc.divide(4, 2));
    }

    @Test
    public void testDivideByZero() {
        assertThrows(ArithmeticException.class, () -> {
            calc.divide(4, 0);
        });
    }
}
```

---

## ▶️ STEP 7: RUN TESTS

```bash
mvn test
```

---

## ✅ EXPECTED OUTPUT

```
Tests run: 3, Failures: 0, Errors: 0
BUILD SUCCESS
```

---

## 📊 RESULT

* Successfully created a Maven project
* Implemented Calculator class
* Executed JUnit test cases
* All test cases passed successfully

---

## 🧠 VIVA QUESTIONS

1. What is JUnit?
   → A framework for testing Java applications

2. What is @Test annotation?
   → Used to define test methods

3. What is assertion?
   → Validates expected vs actual output

4. Name some assertions
   → assertEquals(), assertTrue(), assertThrows()

5. Difference between src/main and src/test
   → main → application code
   → test → test cases

---

## ⚠️ COMMON ERRORS

* Class name and file name mismatch
* Wrong folder structure
* Missing JUnit dependency
* Writing test file in `main` instead of `test`

---

## ✅ CONCLUSION

JUnit helps automate testing, improves code reliability, and is essential in DevOps pipelines.

---
