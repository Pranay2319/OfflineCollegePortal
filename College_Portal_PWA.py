## Question A
### Develop a PWA that works in offline mode using Service Worker.

### offline.html
<!DOCTYPE html>
<html>
<head>
    <title>College Portal</title>
    <style>
        body {
            font-family: Arial;
            background: #f4f6f9;
            margin: 0;
        }

        .header {
            background: #003366;
            color: white;
            text-align: center;
            padding: 10px;
        }

        .container {
            width: 80%;
            margin: auto;
            margin-top: 20px;
        }

        .card {
            background: white;
            padding: 15px;
            margin-top: 15px;
            border-radius: 8px;
        }

        h3 {
            color: #003366;
        }

        button {
            padding: 8px 15px;
            margin: 5px;
            border: none;
            color: white;
            cursor: pointer;
        }

        .blue { background: #007bff; }
        .green { background: #28a745; }
        .red { background: #dc3545; }

        .offline {
            color: red;
            text-align: center;
        }
    </style>
</head>

<body>

<div class="header">
    <h2>Laxmi Charitable Trust's</h2>
    <h3>Sheth L.U.J College</h3>
    <p>College Portal</p>
</div>

<div class="container">

<div class="card">
    <h2 style="text-align:center;">⚠ You are Offline</h2>
    <p class="offline">No Internet Connection</p>
</div>

<div class="card">
    <h3>Student Details</h3>
    <p>Name: Pranay Bhadwalkar</p>
    <p>Roll No: T003</p>
    <p>Class: TYIT</p>
    <p>Batch: 01</p>
</div>

<div class="card">
    <h3>College Info</h3>
    <p>Department: IT</p>
    <p>University: Mumbai University</p>
    <p>Location: Andheri</p>
</div>

<div class="card" style="text-align:center;">
    <h3>Actions</h3>
    <button class="blue">Attendance</button>
    <button class="green">Results</button>
    <button class="blue">Assignments</button>
    <button class="red">Logout</button>
</div>

</div>

</body>
</html>



### service-worker.js
const CACHE = "v1";

self.addEventListener("install", event => {
    event.waitUntil(
        caches.open("offline-cache").then(cache => {
            return cache.addAll([
                "/",
                "/offline.html"
            ]);
        })
    );

    console.log("Service Worker Installed");
});

self.addEventListener("fetch", event => {
    event.respondWith(
        fetch(event.request).catch(() => {
            return caches.match("/offline.html");
        })
    );
});



# Question B
### Create a Student Record Management PWA.

### HomeController.cs

```csharp
using HTMLtoPWA.Models;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;

namespace HTMLtoPWA.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            Student s = new Student();
            s.RollNo = 103;
            s.Name = "Pranay";

            return View(s);
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View();
        }
    }
}


### Student.cs
namespace HTMLtoPWA.Models
{
    public class Student
    {
        public int RollNo { get; set; }

        public string Name { get; set; }
    }
}

### Index.cshtml

@model HTMLtoPWA.Models.Student

<div class="text-center">
    <h1 class="display-4">College Portal</h1>

    <h2>Student Record</h2>

    <p>Roll No : @Model.RollNo</p>
    <p>Name : @Model.Name</p>
</div>


### service-worker.js
const CACHE = "v1";

self.addEventListener("install", e => {
    e.waitUntil(
        caches.open(CACHE).then(cache => {
            return cache.addAll([
                "/",
                "/Home/Index",
                "/offline.html",
                "/css/site.css",
                "/js/site.js"
            ]);
        })
    );
});

self.addEventListener("fetch", e => {
    e.respondWith(
        fetch(e.request).catch(() => {
            return caches.match(e.request).then(response => {
                return response || caches.match("/offline.html");
            });
        })
    );
});
