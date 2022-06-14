using Microsoft.AspNetCore.Mvc;
using System;
using IronPython.Hosting;
using IronPython.Runtime;
using IronPython;
using Microsoft.Scripting.Hosting;
using Microsoft.Scripting;

namespace pySigmaService.Controllers;

[ApiController]
[Route("[controller]")]
public class PySigmaController : ControllerBase
{

    [HttpGet]
    public IActionResult Get()
    {
        var var1 = "hello";
        var var2 = "hello2";

        ScriptEngine engine = Python.CreateEngine();
        ScriptScope scope = engine.CreateScope();
        engine.ExecuteFile(@"~/DP/pySigmaLib/sigma/collection.py", scope);
        dynamic testFunction = scope.GetVariable("from_yaml");
        var result = testFunction(var1, var2);

        return Ok();
    }

}