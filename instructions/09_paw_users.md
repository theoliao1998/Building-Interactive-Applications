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
            rest_path: {"parent":"\/assn","base_url":"https:\/\/www.dj4e.com","controller":"paw_users.md","extra":"","action":false,"parameters":[],"current":"\/assn\/paw_users.md","full":"\/assn\/paw_users.md"},
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
  <option value="paw_users.md" selected>Django Users</option>
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
<h1>Django Users and Authentication</h1>
<p>In this assignment we will add some non-admin users, and the code for them to log in and log out to
the LocalLibrary application.   Then we will add data model elements to represent book checkout and a screen
so users can see the books that they have checked out.</p>
<p><a href="https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication">https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication</a></p>
<p>This is a more complex tutorial so allow plenty of time to work on this tutorial.</p>
<ul>
<li>
<p>You will need an admin user for this assignment, if you have deleted the super user, and need to
create another one, use the following commands in a console shell:</p>
<pre><code>python3 manage.py createsuperuser</code></pre>
</li>
<li>
<p>Make a new user (check the autograder for specific instructions) and add it to Library staff</p>
</li>
<li>
<p>Add the account authentication URLs - make sure to reload your application after you change
the <code>urls.py</code> file.  The MDN tutorial does not remind you each time you need to Reload the application.
Tend toward reloading too often versus not too often.  When in doubt, reload :)
If you are developing locally, it auto-reloads quite a bit but sometimes it is
helpful to abort and restart the <code>runserver</code> command.</p>
</li>
<li>
<p>Update <code>settings.py</code> to add a reference to the new project-wide <code>templates</code> folder - Make
sure to reload your application and test.  When you change configuration files - you might break your entire
application so you want to reload on <em>each</em> configuration change so you can quickly figure out what went
wrong and fix it.  You can use <code>git diff</code> to see what you changes  you have made and if something goes wrong,
you can always revert a file to your previous version and re-make your changes.</p>
<pre><code>get checkout locallibrary/settings.py</code></pre>
<p>Lean on git to keep track of what you have and have not done.</p>
</li>
<li>
<p>After you update <code>urls.py</code>, add the new templates folders</p>
<pre><code>cd ~/django_projects/locallibrary
mkdir templates
mkdir templates/registration</code></pre>
</li>
<li>
<p><code>Reload</code> your application and go to a URL like</p>
<pre><code>http://mdntutorial.pythonanywhere.com/accounts/login/</code></pre>
<p>You will get a 'TemplateDoesNotExist' error - which is correct because the new templates are not there yet.
It should show uyou the name of the template it is looking for.</p>
</li>
<li>
<p>Add the template for <code>login.html</code> in the correct folder as described in the tutorial.  If you successfully
log in without doing the next step - you will be redirected to <code>/accounts/profile/</code> - we need to
change this in the next step.</p>
</li>
<li>
<p>Add the <code>LOGIN_REDIRECT_URL</code> to <code>locallibrary/locallibrary/settings.py</code> as directed in the tutorial and
reload your application.</p>
<pre><code>LOGIN_REDIRECT_URL = '/'</code></pre>
<p>At this point a successful login should go to the '/catalog/' url.</p>
</li>
<li>
<p>You can delay doing the four templates for <code>password_reset</code> until later - the autograder won't check these</p>
</li>
<li>
<p>Update <code>base_generic.html</code> to add the logged in indication as well as Login and Logout links</p>
</li>
<li>
<p>Complete the <a href="https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication#Example_%E2%80%94_listing_the_current_user's_books" target="_blank">Example — listing the current user's books</a>
task - this is pretty intricate and will take some time.  This entails a change to the <code>models.py</code> and
a migration in the command line.  Once you have changed the <code>models.py</code> file, running the following commands
to update the database schema:</p>
<pre><code>cd ~/django_projects/locallibrary/
python3 manage.py makemigrations
python3 manage.py migrate</code></pre>
</li>
<li>
<p>Update the <code>catalog/admin.py</code> file to add code to the <code>BookInstance</code> model and reload your application.</p>
</li>
<li>
<p>Then log into the `/admin' user interface in your application.  Create some new book instances
(the imprint can be any string) some instances out to a user.  Check out several book instances to different users.
Make sure
to set the status to &quot;On Loan&quot;.</p>
</li>
<li>
<p>Edit the <code>catalog/views.py</code> file and add the <code>LoanedBooksByUserListView</code> view.</p>
</li>
<li>
<p>Edit the <code>catalog/urls.py</code> and add the url pattern for the <code>LoanedBooksByUserListView</code>.</p>
</li>
<li>
<p>Edit <code>/catalog/templates/base_generic.html</code> and add the link to <code>my-borrowed</code></p>
</li>
<li>
<p>Restart your web application.</p>
</li>
<li>Check to see if your logged in user can see their own borrowed books.   Make sure the user's book
instances have a status of &quot;On Loan&quot;.</li>
</ul><script src="https://static.tsugi.org/js/jquery-1.11.3.js"></script>
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
