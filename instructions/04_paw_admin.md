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
            rest_path: {"parent":"\/assn","base_url":"https:\/\/www.dj4e.com","controller":"paw_admin.md","extra":"","action":false,"parameters":[],"current":"\/assn\/paw_admin.md","full":"\/assn\/paw_admin.md"},
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
  <option value="paw_admin.md" selected>Django Admin</option>
  <option value="dj4e_load.md">Batch Loading Data</option>
  <option value="paw_home.md">Django Home Page</option>
  <option value="paw_details.md">Django Detail Pages</option>
  <option value="paw_sessions.md">Django Sessions</option>
  <option value="paw_users.md">Django Users</option>
  <option value="paw_forms.md">Django Forms</option>
  <option value="paw_github.md">Using GitHub</option>
  <option value="dj_install.md">Installing Django Locally</option>
  <option value="dj4e_hello.md">Hello World</option>
  <option value="dj4e_autos.md">Autos CRUD</option>
  <option value="dj4e_ads1.md">AdList Milestone #1</option>
  <option value="dj4e_ads2.md">AdList Milestone #2</option>
  <option value="dj4e_ads3.md">AdList Milestone #3</option>
  <option value="dj4e_ads4.md">AdList Milestone #4</option>
</select>
</div>
<h1>Django Admin Site</h1>
<p>Our next step is to explore the LocalLibrary administration web site that
allows us to create, read, update, and delete data in our database.</p>
<p><a href="https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site">https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site</a></p>
<p>If you are submitting this assignment to the DJ4E autograder for this assignment,
it would be a good idea to check the autograder for specific instructions that
the autograder requires for this assignment.</p>
<p>Complete the following sections of the Admin tutorial:</p>
<ul>
<li>Edit <code>~/django_projects/locallibrary/catalog/admin.py</code> and register the four models</li>
<li>Create a superuser (The autograder will ask you to make a second superuser)
Note that it is OK to have more than one super user and you can log in as any
super user and edit or delete the other superuser accounts.</li>
<li>Reload your application under the <code>Web</code> tab in
<a href="https://www.pythonanywhere.com" target="_blank">PythonAnywhere</a></li>
<li>Log in to the admin site.  Insead of using <a href="http://localhost:8000/admin">http://localhost:8000/admin</a>, simply add <code>/admin</code> to the end of
your PythonAnywhere site (i.e. like
<a href="http://mdntutorial.pythonanywhere.com/admin" target="_blank"><a href="http://mdntutorial.pythonanywhere.com/admin">http://mdntutorial.pythonanywhere.com/admin</a></a>.</li>
<li>Create some books (The autograder will ask you to create one specific book and author)</li>
<li>Continue into the Advanced Configuration</li>
<li>Register a Model Admin class</li>
<li>Configure the list views - Note that you need to edit <code>~/django_projects/locallibrary/catalog/models.py</code> at one point</li>
<li>Add the list filter</li>
<li>Organize the detail view layout</li>
<li>Enable inline editing of associated records</li>
</ul>
<p>Just as a reminder, when you are running on PythonAnywhere you <strong>do not need</strong> to do a:</p>
<pre><code>python3 manage.py runserver  # Don't do this on PythonAnywhere</code></pre>
<p>Everytime you make a configuration change.  But if you are running on
PythonAnywhere and make a configuration change you <strong>do</strong> need to
go into the <code>Web</code> tab and <code>Reload</code> the web server to re-read your updated configuration.  There is
not harm in reloading your web on PythonAnywhere application too often.  So when in doubt, reload :)</p>
<h2>Making a Fresh Database</h2>
<p>If you want to experiment a bit and you want to wipe out your database and start over, do the following:</p>
<pre><code>cd ~/django_projects/locallibrary
rm db.sqlite3
python3 manage.py migrate</code></pre>
<p>This will wipe out all of your tables and the data in those tables and create fresh and empty tables.
Note that this process will also wipe out your superuser accounts and all data you have entered.</p>
<p>The <code>db.sqlite3</code> file is a normal file - you can back it up and/or copy over it - just make sure to <code>Reload</code>
your web application when you change your database.</p>
<h2>Some Common Mistakes</h2>
<p>Sometimes students set <code>Debug=False</code> in the <code>locallibrary/settings.py</code> file.
This should be set to <code>True</code>.</p>
<p>Sometimes when commands like</p>
<pre><code>python3 manage.py migrate</code></pre>
<p>run without error, but the web application will not start on
PythonAnywhere, check to make sure your virtual environment is
properly set under the Web tab.  If you did the
<a href="paw_install.md" target="_blank">installation</a>
properly and created a <code>django2</code>
virtual environment, the virtual environment should be set to:</p>
<pre><code>/home/drchuck/.virtualenvs/django2</code></pre>
<p>Replacing &quot;drchuck&quot; with your PythonAnywhere account name.</p><script src="https://static.tsugi.org/js/jquery-1.11.3.js"></script>
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
