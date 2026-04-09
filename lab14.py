# 🔬 EXPERIMENT 14: Test Coverage using JaCoCo (Updated & Final)

---

## 🎯 AIM

To measure software code quality by evaluating test coverage using JaCoCo tool.

---

## 🧠 THEORY

* **JaCoCo (Java Code Coverage)** is a tool used to analyze how much of the code is executed during testing.
* It provides metrics such as:

  * Line Coverage
  * Branch Coverage
  * Method Coverage
  * Class Coverage
* Higher coverage indicates better testing and reliability.

---

## 🛠️ TOOLS REQUIRED

* Java JDK (11 or above)
* Maven
* IDE (IntelliJ / Eclipse)
* JaCoCo Maven Plugin

---

## 📁 STEP 1: USE EXISTING PROJECT

Navigate to project directory:

```bash
cd junit-demo
```

---

## ⚙️ STEP 2: UPDATE pom.xml

Open `pom.xml` and ensure:

### 🔹 JUnit Dependency:

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

### 🔹 Add JaCoCo Plugin inside `<build>`:

```xml
<build>
    <plugins>

        <!-- JaCoCo Plugin -->
        <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.11</version>
            <executions>

                <!-- Attach JaCoCo agent -->
                <execution>
                    <goals>
                        <goal>prepare-agent</goal>
                    </goals>
                </execution>

                <!-- Generate report -->
                <execution>
                    <id>report</id>
                    <phase>test</phase>
                    <goals>
                        <goal>report</goal>
                    </goals>
                </execution>

            </executions>
        </plugin>

    </plugins>
</build>
```

---

## ▶️ STEP 3: RUN TEST WITH COVERAGE

```bash
mvn clean test
```

---

## 📊 STEP 4: VERIFY BUILD OUTPUT

Expected:

```text
BUILD SUCCESS
Tests run: 3, Failures: 0
jacoco:report executed
```

---

## 📁 STEP 5: LOCATE COVERAGE FILES

JaCoCo generates:

```text
target/jacoco.exec        → raw coverage data
target/site/jacoco/       → HTML report
```

---

## 🌐 STEP 6: VIEW REPORT

Open in browser:

```text
target/site/jacoco/index.html
```

---

## 📊 STEP 7: ANALYZE COVERAGE

You will see:

* Instruction Coverage
* Line Coverage
* Branch Coverage
* Method Coverage
* Class Coverage

Example:

```text
Line Coverage: ~100%
Branch Coverage: ~100% (after exception test)
```

---

## 🔄 STEP 8: IMPROVE COVERAGE (IF NEEDED)

Ensure all scenarios are tested:

```java
@Test
public void testDivideByZero() {
    assertThrows(ArithmeticException.class, () -> {
        calc.divide(4, 0);
    });
}
```

---

## 📊 RESULT

* JaCoCo successfully measured code coverage
* Coverage report generated in HTML format
* Test quality improved by covering edge cases
