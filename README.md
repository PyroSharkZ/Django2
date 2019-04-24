# Django Tutorials

Django is a python based web framework used to create websites or webservers.

One element of Django is templates, the templating system is when you inject in text and it outputs the result. The template engine within the Django context - inject stuff like <h1>{ } title {} </h1> will become (this is where the templating engine does its work)
<h1> Actual Title </h1>
Text in, text out ^

A second feature of Django is ORM (Object Relational Mapper).
There needs to be a Python class which we provide and it outputs an SQL table.


The third element of Django is Rooting. It takes an URL and activates a Python function, a callable.
User types in the URL, gets sent to the server, after some point it activates a Python code of some sort. It is the decoder.

The final element of Django is Views. Pure Python, so it's the logic. It always accepts requests and always sends out a response. The response or exepction is usually to render the template with some data - but it could be something else.

# Django Terminology