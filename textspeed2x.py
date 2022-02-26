import yttranscripts
import hft
import extract_keywords
import extract_sentences

webpage = "https://en.wikipedia.org/wiki/Hrithik_Roshan"
opt = 1
youtube = "sAzL4XMke80"
# youtube= "IOyq-eTRhvo"
file_name="input.txt"
text="""The best approach to be the fastest tester is writing less code. And we can use different built automation tools. In my opinion, 2022 will dominate two big tools: Maven and Gradle. Maven is a software project management and comprehension tool. Based on the concept of a project object model (POM). Maven can manage dependencies flexibly, namely, load third-party libraries into its local repository, select the required package version, and handle transitive dependencies.
Maven doesn't depend on the operating system, since it ignores the specifics of working in the platform command line. Plus, Maven has several repositories: local, central, and remote. Gradle is an open-source build automation tool focused on flexibility and performance through Apache Ant and Apache Maven concepts. It allows you to dynamically create tasks, maintain the software life cycle, and use the code's logic to build the project, making it more flexible. Gradle is ideal for supporting multi-project builds by allowing you to define the order to execute tasks.
Libraries
We need Java libraries to speed up the development process, making writing this code more
concise and enjoyable. Java libraries don't affect or impose any restrictions on the
architecture of a software product. Furthermore, they can be used as a set of subroutines
close to their functionality. Today there are a considerable number of libraries.
Selenium
It's not the first year that one of the most popular Selenium libraries has been ranked top.The amount of web content is overgrowing, and the easiest way to automate testing is tostart with a time-tested library. Therefore, Selenium continues to be the very library thatautomated testing beginners can start. Moreover, Selenium is widely used to build itsframeworks and create its test automation products by many companies.
Today's Selenium ecosystem consists of three main parts:
The first and most important is Selenium WebDriver, which helps create automatictest suites and test cases to scale across different testing environments.
The second part is the Selenium IDE, which makes and allows not complexautomated scripts to pass various scenarios at the initial stages.
The last one is Selenium Grid, a server that enables management tests on differentenvironments from one central repository, simplifying launch and maintenance.
Selenide
Selenide is an intelligent add-on over Selenium WebDriver that uses all its advantages andallows you to minimize the amount of code by reusing the repetitive code in separateclasses. Additional benefits include Ajax support for stabilizing autotests, as well as powerful selectors that allow you to accurately find the desired element even in a very complexproject with a branched and dynamically changing DOM (Document Object Model)architecture. Besides, Selenide has a relatively simple configuration, making it easier andfaster to write automated tests for beginners and professionals.
Selenoid
Selenoid is a server that allows you to run dozens of tests simultaneously in browsers indocker containers. Selenoid has a very high performance, which is superior to SeleniumGrid. Ease of installation and deployment is another of Selenoid's advantages; it also scalesand updates quickly. Thanks to work in docker containers, each browser starts clean and isolated from the primary system and consumes no more than 20 megabytes of RAM(Random-access memory) in a standby state.
TestNG
TestNG is a testing framework based on JUnit (Java) and NUnit (C #); it has been popularwith Java testers for quite a long time. In 2022, it will also be in wide demand due to its usefor Unit testing, functional testing, integration testing, and end-to-end testing.One of the main factors in the continued use of this framework is that many projects havealready been written using it. Multiple annotations and the ability to use a parameterization ofautotests make it more flexible and easily adaptable to any needs of a tester.
Cucumber
The following framework that will also be popular in 2022 is Cucumber. Its popularity isbecause tests are written in an ordinary language understandable for autotests and peoplefar from development and testing, for example, analysts and project managers. Cucumberuses a BDD (Behavior-Driven Development) approach; it allows third-party people to createcustom scripts, which increases the quality and coverage of autotests.
JUnit
JUnit is designed for unit testing and will be very popular in 2022 due to the growing numberof projects on microservice architecture. TDD (Test-Driven Development) technic allows it totake a leading position, reducing the risk of errors at the earliest stage, when there is nocode yet. With the release of the new version of JUnit 5, which introduces parameters andassertions, the creation of autotests goes to an entirely new level, allowing you to carry outchecks in those cases where it was previously impossible.
Lombok
The Lombok library reduces the amount of code you write, improving its readability. It won'tbe difficult to add it to the project, and it only needs to be done once.Lombok also generates code at the compilation stage, speeding up the process of passingautotests and increasing their stability."""

if opt <= 1:
    print(hft.hugging_face(webpage,opt))
elif opt == 2:
     print(hft.hugging_face(yttranscripts.youtube_cap(youtube),0))
elif opt==3:
    print(extract_keywords.Keywords(text))
elif opt==4:
    print(extract_sentences.generate_summary(file_name))