using FizzBuzzSol;
using NUnit.Framework;

namespace FizzBuzzTest;

public class Tests
{
    [SetUp]
    public void Setup()
    {
    }

    [Test]
    public void IsMultOfThreeFizz()
    {
        string[] testFizz = FizzBuzzProgram.FizzBuzz(5);
        Assert.That(testFizz[2], Is.EqualTo("Fizz"));
    }

    [Test]
    public void IsMultOfFiveBuzz()
    {
        string[] testFizz = FizzBuzzProgram.FizzBuzz(5);
        Assert.That(testFizz[4], Is.EqualTo("Buzz"));
    }

    [Test]
    public void IsMultOfThreeAndFiveFizzBuzz()
    {
        string[] testFizz = FizzBuzzProgram.FizzBuzz(20);
        Assert.That(testFizz[14], Is.EqualTo("FizzBuzz"));
    }
}