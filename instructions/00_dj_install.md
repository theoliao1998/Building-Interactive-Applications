<!DOCTYPE html>
    <html>
      <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DJ4E - Django for Everybody</title>
        <script>
        var _TSUGI = {
            context_title: "SI 664 001 FA 2019",
            link_title: "Tool: Autograder: Request-Response Cycle",
            user_displayname: "Xinhao Liao",
            user_locale: "en",
            ajax_session: false,
            heartbeat: 1500000,
            heartbeat_url: "https://www.dj4e.com/tsugi/util/heartbeat?msec=1500000",
            rest_path: {"parent":"\/assn","base_url":"https:\/\/www.dj4e.com","controller":"dj_install.md","extra":"","action":false,"parameters":[],"current":"\/assn\/dj_install.md","full":"\/assn\/dj_install.md"},
            spinnerUrl: "https://static.tsugi.org/img/spinner.gif",
            staticroot: "https://static.tsugi.org",
            websocket_url: false,
            websocket_token: false,
            window_close_message: "Application complete",
            session_expire_message: "Your session has expired"
        }
        </script>
        <!-- Tiny bit of JS -->
        <script src="https://static.tsugi.org/js/tsugiscripts_head.js"></script>
        <!-- Le styles -->
        <link href="https://static.tsugi.org/bootstrap-3.4.1/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://static.tsugi.org/js/jquery-ui-1.11.4/jquery-ui.min.css" rel="stylesheet">
                <link href="https://static.tsugi.org/fontawesome-free-5.8.2-web/css/all.css" rel="stylesheet">
        <link href="https://static.tsugi.org/fontawesome-free-5.8.2-web/css/v4-shims.css" rel="stylesheet">
        <style>:root {--primary:#0D47A1;--primary-border:#0d4295;--primary-darker:#0c4091;--primary-darkest:#0b3b85;--secondary:#EEEEEE;--text:#111111;--text-light:#5E5E5E;--font-family:sans-serif;--font-size:14px;}</style>
          <link href="https://static.tsugi.org/css/tsugi.css" rel="stylesheet">

          <style>
                        </style>
<style>
a[target="_blank"]:after {
    font-family: 'Font Awesome 5 Free';
    font-weight: 600;
    content: " \f35d";
}
.goog-te-banner-frame.skiptranslate {
    display: none !important;
    }
body {
    top: 0px !important;
    }
</style>

        <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
          <script src="https://www.dj4e.com/tsugi/vendor/tsugi/lib/static/js/html5shiv/html5shiv.js"></script>
          <script src="https://www.dj4e.com/tsugi/vendor/tsugi/lib/static/js/respond/respond.min.js"></script>
        <![endif]-->

    <script type="text/javascript">CSRF_TOKEN = "5dbde64861f20";</script>
</head>
<body prefix="oer: http://oerschema.org">
<div id="body_container">
<script>
if (window!=window.top) {
    document.getElementById("body_container").className = "container-fluid";
} else {
    document.getElementById("body_container").className = "container";
}
</script>
<nav class="navbar navbar-inverse navbar-fixed-top" role="navigation" id="tsugi_main_nav_bar" style="display:none">  <div class="container-fluid">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="https://www.dj4e.com">DJ4E</a>
    </div>
    <div class="navbar-collapse collapse">
      <ul class="nav navbar-nav navbar-main">
        <li><a href="https://www.dj4e.com/lessons" >Lessons</a></li>
        <li><a href="https://www.dj4e.com/assn" >Assignments</a></li>
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="http://www.dr-chuck.com" target="_blank" >Instructor</a></li>
        <li><a href="https://www.dj4e.com/tsugi/login.php" >Login</a></li>
      </ul>
    </div> <!--/.nav-collapse -->
  </div> <!--container -->
</nav>
<script>
if ( ! inIframe() ) {
  document.getElementById('tsugi_main_nav_bar').style.display = 'block';
  document.getElementsByTagName('body')[0].style.paddingTop = '5.93rem';
}
</script>
<div id="flashmessages"></div><style>
center {
    padding-bottom: 10px;
}
@media print {
    #chapters {
        display: none;
    }
}
a[target="_blank"]:after {
  content: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAQElEQVR42qXKwQkAIAxDUUdxtO6/RBQkQZvSi8I/pL4BoGw/XPkh4XigPmsUgh0626AjRsgxHTkUThsG2T/sIlzdTsp52kSS1wAAAABJRU5ErkJggg==);
  margin: 0 3px 0 5px;
}
</style>
</head>
<body prefix="oer: http://oerschema.org">
<div id="body_container">
<script>
if (window!=window.top) {
    document.getElementById("body_container").className = "container-fluid";
} else {
    document.getElementById("body_container").className = "container";
}
</script>
<script>
function onSelect() {
    console.log($('#chapters').val());
    window.location = $('#chapters').val();
}
</script>
<div style="float:right">
<select id="chapters" onchange="onSelect();">
  <option value="paw_install.md">Django and PythonAnywhere</option>
  <option value="paw_skeleton.md">Skeleton web site</option>
  <option value="paw_models.md">Django Models</option>
  <option value="paw_admin.md">Django Admin</option>
  <option value="dj4e_load.md">Batch Loading Data</option>
  <option value="paw_home.md">Django Home Page</option>
  <option value="paw_details.md">Django Detail Pages</option>
  <option value="paw_sessions.md">Django Sessions</option>
  <option value="paw_users.md">Django Users</option>
  <option value="paw_forms.md">Django Forms</option>
  <option value="paw_github.md">Using GitHub</option>
  <option value="dj_install.md" selected>Installing Django Locally</option>
  <option value="dj4e_hello.md">Hello World</option>
  <option value="dj4e_autos.md">Autos CRUD</option>
  <option value="dj4e_ads1.md">AdList Milestone #1</option>
  <option value="dj4e_ads2.md">AdList Milestone #2</option>
  <option value="dj4e_ads3.md">AdList Milestone #3</option>
  <option value="dj4e_ads4.md">AdList Milestone #4</option>
</select>
</div>
<h1>Developing with Django on your computer</h1>
<p>As you start to develop more intricate Django applications, you might find it more
convienent to install Django on your local computer and then use github to move your
tested code into your
<a href="https://www.pythonanywhere.com" target="_blank">PythonAnywhere</a>
server so you it is available on the Internet for grading or otherwise sharing.</p>
<p>There are many sources of tutorial material on how to install Python3 and Django on
your computer.  Since the rest of this material uses the Mozilla Developer Network
tutorials, you might as well use it:</p>
<p><a href="https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment">https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment</a></p>
<p>You can use a virtual environment or if you have a suitable version of Python 3.x on your
computer and can use <code>pip3</code> to install a suitable version of Django for your whole computer,
there is no need to put things in a virtual environment.</p>
<p>Also you should install git on your computer using any of the good tutorials out there.</p>
<p>You know Python and Django are correctly installed when these commands
show reasonable version numbers:</p>
<p>Linux/Mac:</p>
<pre><code>$ python3 --version
Python 3.6.0
$ python3 -m django --version
2.0.5</code></pre>
<p>If the above does not work on Windows, try:</p>
<pre><code>&gt; py --version
Python 3.6.0
&gt; py -m django --version
2.0.5</code></pre>
<p>You also need to have <code>git</code> installed and available in the shell / command line.</p>
<h2>Why Develop Locally?</h2>
<p>There are a number of advantages to doing development work locally:</p>
<ul>
<li>
<p>You never have to <code>Reload</code> your application.  The Django <code>runserver</code> process monitors
changes to your files and completely restarts itself as soon as any file changes in your
project.   This makes for much quicker edit-test cycles.</p>
</li>
<li>
<p>You can use a fancy text editor like VScode, Atom, or Sublime.</p>
</li>
<li>
<p>No more need to change the WGSI configuration file when you want to switch between
your project and some sample code - you can even run more than one application at the
same time on different ports.</p>
</li>
<li>
<p>You can put debug <code>print()</code> statements and they come right out without having to look
at the error or server logs.  Error tracebacks and error logs come right out.</p>
</li>
<li>You can work without a network connection!</li>
</ul>
<p>These instructions assume you that you are already set up using Github and PythonAnywhere
and want to edit your applications on your computer
and present them on PythonAnywhere.  But you can always use the
<a href="../ngrok">ngrok</a> application
to submit your assignments to the autograder if you like.</p>
<h2>On Your Laptop</h2>
<p>We suggest you make a folder somewhere to store all of your Django projects.  This folder
should be easy to find so you can use your cool VSCode, Atom, or Sublime text editor.</p>
<p>Linux / MacOS / Windows bash shell:</p>
<pre><code>cd ~
cd Desktop
mkdir django</code></pre>
<p>Windows Command Line:</p>
<pre><code>cd
cd Desktop
mkdir django</code></pre>
<p>Then lets checkout the dj4e-samples repo and get things started:</p>
<pre><code>cd Desktop      # If not already there
cd django
git clone https://github.com/csev/dj4e-samples

cd dj4e-samples
python3 manage.py migrate            # Makemigrations is already in git
python3 manage.py createsuperuser
python3 manage.py runscript gview_load
python3 manage.py runscript many_load</code></pre>
<p>To run the server get into the folder with <code>manage.py</code> and then:</p>
<pre><code>python3 manage.py runserver</code></pre>
<p>Then navigate to <a href="http://localhost:8000">http://localhost:8000</a> to see the page.</p>
<p>Then just for fun, open a second terminal / shell / command line and:</p>
<pre><code>cd Desktop
cd django
cd dj4e-samples
python3 manage.py runserver 8001</code></pre>
<p>Then navigate to <a href="http://localhost:8001">http://localhost:8001</a> to see the page.</p>
<p>You can abort the <code>runserver</code> applications in the command line, switch to
a new folder and start runserver again.</p>
<p>This section shows how to get a Django application working - in the next section
we show you to work on your code on two computers and move
the changes back and forth.</p>
<h2>Moving Code Between Your Laptop and PythonAnywhere</h2>
<p>If you want, you can keep a local copy your <code>django_projects</code> synchronized with your
copy on PythonAnywhere using <code>github</code>.</p>
<h2>If you are already using github to store your projects</h2>
<p>Before you start doing this, make sure that your code in the PythonAnywhere shell
is fully checked in to GitHub:</p>
<pre><code>$ cd ~/django_projects
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working directory clean</code></pre>
<p>If you have any outstanding git modifications on PYAW - clean it up and push it to the repo.</p>
<h2>If you have not yet put your PythonAnywhere code on github</h2>
<p>If you have not yet uploaded your <code>django_projects</code> folder to github, first follow the
<a href="paw_github.md">these instructions</a> to get your application uploaded to github.</p>
<h2>Checking your github code out onto your laptop</h2>
<p>Once your application is in github, you can simply check it out to your laptop computer
using commands like:</p>
<pre><code>cd ~         # or simple 'cd' for Windows
cd Desktop
cd django
git clone https://github.com/drchuck/django_projects.git</code></pre>
<p>Replacing <code>drchuck</code> with your github account.  This should bring a copy of your
application from github down to your computer and store it in the folder
<code>django_projects</code>.</p>
<p>Note that you should keep the <code>dj4e-samples</code> and <code>django_projects</code> next to each
other since they are both in github.</p>
<p>On your laptop:</p>
<pre><code>Desktop/django/dj4e-samples
Desktop/django/django_projects</code></pre>
<p>On PythonAnywhere:</p>
<pre><code>~/dj4e-samples
~/django_projects</code></pre>
<h2>Working on your Code on your Laptop</h2>
<p>So you are on your local laptop / computer and are making changes</p>
<pre><code>cd ~         # or simple 'cd' for Windows
cd Desktop
cd django
cd django_projects
cd locallibrary    # Or whatever project you want to work on
# edit some files :)
python3 manage.py makemigrations    # If you changed your models
python3 manage.py migrate           # If you changed your models.py
git status
git add ....
git commit -a
git push</code></pre>
<p>Then you can go into PythonAnywhere in a bash shell and type:</p>
<pre><code>cd ~/django_projects/locallibrary
git pull
python3 manage.py migrate         # If the pull included new migrations</code></pre>
<p>Then in the &quot;Web&quot; tab reload your application and visit it.</p>
<p>As long as you follow the pattern of doing <code>git push</code> from your laptop/desktop and <code>git pull</code>
from PythonAnywhere, things will go very smoothly.</p>
<p>If you edit two places and push from one of the places, the push will work - but the push
won't work from the second place and pull won't work either becausee you have local changes.
If this is what you did, there is a simple workaround.  On the system where you have un-pushed
changes and want to do a pull before pushing, do this:</p>
<pre><code>git stash
git pull
git stash apply</code></pre>
<p>This takes your un-pushed changes and hides them in the &quot;stash&quot;, allowing the <code>git pull</code> to
work and then the <code>stash apply</code> re-modifies the files.</p>
<p>Most of the time this works if all you did is edited two places and tried to push from both.</p><script src="https://static.tsugi.org/js/jquery-1.11.3.js"></script>
<script src="https://static.tsugi.org/bootstrap-3.4.1/js/bootstrap.min.js"></script>
<script src="https://static.tsugi.org/js/jquery-ui-1.11.4/jquery-ui.min.js"></script>
<script src="https://static.tsugi.org/js/jquery.timeago-1.6.3.js"></script>
<script src="https://static.tsugi.org/js/handlebars-v4.0.2.js"></script>
<script src="https://static.tsugi.org/tmpljs-3.8.0/tmpl.min.js"></script>
<script src="https://static.tsugi.org/js/tsugiscripts.js"></script>
<script type="text/javascript">
    HEARTBEAT_TIMEOUT = setTimeout(doHeartBeat, _TSUGI.heartbeat);
    tsugiEmbedMenu();
</script>
<div id="google_translate_element" style="position: fixed; right: 1em; bottom: 0.25em;"></div><script type="text/javascript">
function googleTranslateElementInit() {
  new google.translate.TranslateElement({pageLanguage: "en", layout: google.translate.TranslateElement.InlineLayout.SIMPLE
    }, "google_translate_element");
}
</script><script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
<script>
// PHP VERSION 7.0 and 7.1 HACK
// https://stackoverflow.com/questions/44980654/how-can-i-make-trans-sid-cookie-less-sessions-work-in-php-7-1
$('a').each(function (x) {
    var href = $(this).attr('href');
    if ( ! href ) return;
    if ( ! href.startsWith('#') ) return;
    var pos = href.indexOf('/?');
    if ( pos < 1 ) return;
    console.dir('Patching broken # href='+href);
    href = href.substring(0,pos);
    $(this).attr('href', href);
});

</script>
<script>
// https://stackoverflow.com/questions/7901679/jquery-add-target-blank-for-outgoing-link
$(window).load(function() {
    $('a[href^="http"]').attr('target', function() {
      if(this.host == location.host) return '_self'
      else return '_blank'
    });
});
</script>

</div></body>
</html>
