#!/bin/bash

javac -cp /Users/nathanjohnson/methods-spring-2024/problems/sumofprimes/java/nathanjohnson/junit-4.13.2.jar sumOfPrimes.java
java -cp /Users/nathanjohnson/methods-spring-2024/problems/sumofprimes/java/nathanjohnson/junit-4.13.2.jar:. sumOfPrimes $1