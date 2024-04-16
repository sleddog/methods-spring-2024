using Microsoft.OpenApi.Models;
using FizzBuzzSol;
using Microsoft.AspNetCore.Mvc;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen(c =>
   {
       c.SwaggerDoc("v1", new OpenApiInfo { Title = "FizzBuzz API", Description = "Get Responses from FizzBuzz", Version = "v1" });
   });

var app = builder.Build();
app.UseSwagger();
app.UseSwaggerUI(c =>
   {
     c.SwaggerEndpoint("/swagger/v1/swagger.json", "FizzBuzz API V1");
   });

app.UseDefaultFiles();
app.UseStaticFiles();

app.MapPost("/fizzbuzz", ([FromForm] int number) => 
    {
        return FizzBuzzProgram.FizzBuzz(number);

    }).DisableAntiforgery();
app.Run();
