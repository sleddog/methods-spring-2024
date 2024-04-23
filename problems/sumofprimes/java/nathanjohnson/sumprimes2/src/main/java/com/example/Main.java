package com.example;
import java.io.File;

//import io.jooby.Jooby;
//import io.jooby.ServerOptions;
import io.jooby.Jooby;
import io.jooby.ServerOptions;


public class Main {
    public static void main(String[] args) {
        Jooby app = new Jooby();
        app.setServerOptions(new ServerOptions().setPort(8080));

        app.get("/", ctx -> {
            return new File("src/main/resources/frontEnd.html");
        });

        app.post("/primeSumOutput", ctx -> {
            String integerInput = ctx.form("textBox").value();
            int intPost = Integer.parseInt(integerInput);
            return "The sum of primes from 0 to " + intPost + " is " + sumOfPrimes.primeSum(intPost) + ".";
        });

        app.start();
    }
}