<!DOCTYPE html>
<!-- saved from url=(0034)http://localhost:8890/edit/app.py# -->
<html lang="en-us"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    

    <title>app.py - Jupyter Text Editor</title>
    <link id="favicon" rel="shortcut icon" type="image/x-icon" href="http://localhost:8890/static/base/images/favicon-file.ico?v=f9f0a782d7d67b3a57bf7dce251d771b405c7890604576ec8b9a621a39d7670f6b43ffabef1e566f1cd741ee302e15977d9e1cf60bbacebafe75787b9916415c">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="./app_files/jquery-ui.min.css" type="text/css">
    <link rel="stylesheet" href="./app_files/jquery.typeahead.min.css" type="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    
<link rel="stylesheet" href="./app_files/codemirror.css">
<link rel="stylesheet" href="./app_files/dialog.css">

    <link rel="stylesheet" href="./app_files/style.min.css" type="text/css">
    

    <link rel="stylesheet" href="./app_files/custom.css" type="text/css">
    <script src="./app_files/promise.min.js.download" type="text/javascript" charset="utf-8"></script>
    <script src="./app_files/react.production.min.js.download" type="text/javascript"></script>
    <script src="./app_files/react-dom.production.min.js.download" type="text/javascript"></script>
    <script src="./app_files/index.js.download" type="text/javascript"></script>
    <script src="./app_files/require.js.download" type="text/javascript" charset="utf-8"></script>
    <script>
      require.config({
          
          urlArgs: "v=20250303164824",
          
          baseUrl: '/static/',
          paths: {
            'auth/js/main': 'auth/js/main.min',
            custom : '/custom',
            nbextensions : '/nbextensions',
            kernelspecs : '/kernelspecs',
            underscore : 'components/underscore/underscore-min',
            backbone : 'components/backbone/backbone-min',
            jed: 'components/jed/jed',
            jquery: 'components/jquery/jquery.min',
            json: 'components/requirejs-plugins/src/json',
            text: 'components/requirejs-text/text',
            bootstrap: 'components/bootstrap/dist/js/bootstrap.min',
            bootstraptour: 'components/bootstrap-tour/build/js/bootstrap-tour.min',
            'jquery-ui': 'components/jquery-ui/dist/jquery-ui.min',
            moment: 'components/moment/min/moment-with-locales',
            codemirror: 'components/codemirror',
            termjs: 'components/xterm.js/xterm',
            typeahead: 'components/jquery-typeahead/dist/jquery.typeahead.min',
          },
          map: { // for backward compatibility
              "*": {
                  "jqueryui": "jquery-ui",
              }
          },
          shim: {
            typeahead: {
              deps: ["jquery"],
              exports: "typeahead"
            },
            underscore: {
              exports: '_'
            },
            backbone: {
              deps: ["underscore", "jquery"],
              exports: "Backbone"
            },
            bootstrap: {
              deps: ["jquery"],
              exports: "bootstrap"
            },
            bootstraptour: {
              deps: ["bootstrap"],
              exports: "Tour"
            },
            "jquery-ui": {
              deps: ["jquery"],
              exports: "$"
            }
          },
          waitSeconds: 30,
      });

      require.config({
          map: {
              '*':{
                'contents': 'services/contents',
              }
          }
      });

      // error-catching custom.js shim.
      define("custom", function (require, exports, module) {
          try {
              var custom = require('custom/custom');
              console.debug('loaded custom.js');
              return custom;
          } catch (e) {
              console.error("error loading custom.js", e);
              return {};
          }
      })

      // error-catching custom-preload.js shim.
      define("custom-preload", function (require, exports, module) {
          try {
              var custom = require('custom/custom-preload');
              console.debug('loaded custom-preload.js');
              return custom;
          } catch (e) {
              console.error("error loading custom-preload.js", e);
              return {};
          }
      })

    document.nbjs_translations = {"domain": "nbjs", "locale_data": {"nbjs": {"": {"domain": "nbjs"}}}};
    document.documentElement.lang = navigator.language.toLowerCase();
    </script>

    
    

<script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="services/contents" src="./app_files/contents.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="custom/custom-preload" src="./app_files/custom-preload.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="custom/custom" src="./app_files/custom.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="codemirror/mode/python/python" src="./app_files/python.js.download"></script></head>

<body class="edit_app " data-base-url="/" data-file-path="app.py" data-jupyter-api-token="d07a0e09e0801317ebba5a7c31296a9d40327e207f411c72" dir="ltr">

<noscript>
    <div id='noscript'>
      Jupyter Notebook requires JavaScript.<br>
      Please enable it to proceed. 
  </div>
</noscript>

<div id="header" role="navigation" aria-label="Top Menu" style="display: block;">
  <div id="newsId" style="display: inline;">
    
    <div class="alert alert-info" role="alert">
      <div style="display: flex">
        <div>
          <span class="label label-warning">UPDATE</span>
          Read <a href="https://jupyter-notebook.readthedocs.io/en/latest/migrate_to_notebook7.html" style="text-decoration: underline;" target="_blank">the migration plan</a> to Notebook 7 to learn about the new features and the actions to take if you are using extensions
          -
          Please note that updating to Notebook 7 might break some of your extensions.
        </div>
        <div style="margin-left: auto;">
          <a href="http://localhost:8890/edit/app.py" onclick="alert(&#39;This message will not be shown anymore.&#39;); return false;">
            <button type="button" class="btn btn-default btn-xs" id="dontShowId">
              Don't show anymore
            </button>
          </a>
        </div>
      </div>
    </div>
    
  </div>
  <div id="header-container" class="container">
  <div id="ipython_notebook" class="nav navbar-brand"><a href="http://localhost:8890/tree?token=d07a0e09e0801317ebba5a7c31296a9d40327e207f411c72" title="dashboard">
      <img src="./app_files/logo.png" alt="Jupyter Notebook">
  </a></div>

  

<span id="save_widget" class="pull-left save_widget">
    <span class="filename">app.py</span>
    <div class="dirty-indicator-clean" title="No changes to save"></div><span class="last_modified" title="Mon, Mar 3, 2025 5:39 PM">a few seconds ago</span>
</span>


  

  
  
  
  

    <span id="login_widget">
      
        <button id="logout" class="btn btn-sm navbar-btn">Logout</button>
      
    </span>

  

  
  
  </div>
  <div class="header-bar"></div>

  

<div id="menubar-container" class="container">
  <div id="menubar">
    <div id="menus" class="navbar navbar-default" role="navigation">
      <div class="container-fluid">
          <p class="navbar-text indicator_area">
          <span id="current-mode" title="The current language is Python">Python</span>
          </p>
        <button type="button" class="btn btn-default navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
          <i class="fa fa-bars"></i>
          <span class="navbar-text">Menu</span>
        </button>
        <ul class="nav navbar-nav navbar-right">
          <li id="notification_area"><div id="notification_save" class="notification_widget btn btn-xs navbar-btn" style="display: none;"><span></span></div></li>
        </ul>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li class="dropdown"><a href="http://localhost:8890/edit/app.py#" class="dropdown-toggle" data-toggle="dropdown" aria-expanded="false">File</a>
              <ul id="file-menu" class="dropdown-menu">
                <li id="new-file"><a href="http://localhost:8890/edit/app.py#">New</a></li>
                <li id="save-file"><a href="http://localhost:8890/edit/app.py#">Save</a></li>
                <li id="rename-file"><a href="http://localhost:8890/edit/app.py#">Rename</a></li>
                <li id="download-file"><a href="http://localhost:8890/edit/app.py#">Download</a></li>
              </ul>
            </li>
            <li class="dropdown"><a href="http://localhost:8890/edit/app.py#" class="dropdown-toggle" data-toggle="dropdown">Edit</a>
              <ul id="edit-menu" class="dropdown-menu">
                <li id="menu-find"><a href="http://localhost:8890/edit/app.py#">Find</a></li>
                <li id="menu-replace"><a href="http://localhost:8890/edit/app.py#">Find &amp; Replace</a></li>
                <li class="divider"></li>
                <li class="dropdown-header">Key Map</li>
                <li id="menu-keymap-default" class="selected-keymap"><a href="http://localhost:8890/edit/app.py#">Default<i class="fa"></i></a></li>
                <li id="menu-keymap-sublime"><a href="http://localhost:8890/edit/app.py#">Sublime Text<i class="fa"></i></a></li>
                <li id="menu-keymap-vim"><a href="http://localhost:8890/edit/app.py#">Vim<i class="fa"></i></a></li>
                <li id="menu-keymap-emacs"><a href="http://localhost:8890/edit/app.py#">emacs<i class="fa"></i></a></li>
              </ul>
            </li>
            <li class="dropdown"><a href="http://localhost:8890/edit/app.py#" class="dropdown-toggle" data-toggle="dropdown">View</a>
              <ul id="view-menu" class="dropdown-menu">
              <li id="toggle_header" title="Show/Hide the logo and notebook title (above menu bar)">
              <a href="http://localhost:8890/edit/app.py#">Toggle Header</a></li>
              <li id="menu-line-numbers"><a href="http://localhost:8890/edit/app.py#">Toggle Line Numbers</a></li>
              </ul>
            </li>
            <li class="dropdown"><a href="http://localhost:8890/edit/app.py#" class="dropdown-toggle" data-toggle="dropdown">Language</a>
              <ul id="mode-menu" class="dropdown-menu">
              <li><a href="http://localhost:8890/edit/app.py#" title="Set language to APL">APL</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to PGP">PGP</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to ASN.1">ASN.1</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Asterisk">Asterisk</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Brainfuck">Brainfuck</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to C">C</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to C++">C++</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Cobol">Cobol</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to C#">C#</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Clojure">Clojure</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to ClojureScript">ClojureScript</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Closure Stylesheets (GSS)">Closure Stylesheets (GSS)</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to CMake">CMake</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to CoffeeScript">CoffeeScript</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Common Lisp">Common Lisp</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Cypher">Cypher</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Cython">Cython</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Crystal">Crystal</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to CSS">CSS</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to CQL">CQL</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to D">D</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Dart">Dart</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to diff">diff</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Django">Django</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Dockerfile">Dockerfile</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to DTD">DTD</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Dylan">Dylan</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to EBNF">EBNF</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to ECL">ECL</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to edn">edn</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Eiffel">Eiffel</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Elm">Elm</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Embedded Javascript">Embedded Javascript</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Embedded Ruby">Embedded Ruby</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Erlang">Erlang</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Esper">Esper</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Factor">Factor</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to FCL">FCL</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Forth">Forth</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Fortran">Fortran</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to F#">F#</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Gas">Gas</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Gherkin">Gherkin</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to GitHub Flavored Markdown">GitHub Flavored Markdown</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Go">Go</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Groovy">Groovy</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to HAML">HAML</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Haskell">Haskell</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Haskell (Literate)">Haskell (Literate)</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Haxe">Haxe</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to HXML">HXML</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to ASP.NET">ASP.NET</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to HTML">HTML</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to HTTP">HTTP</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to IDL">IDL</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Pug">Pug</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Java">Java</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Java Server Pages">Java Server Pages</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to JavaScript">JavaScript</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to JSON">JSON</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to JSON-LD">JSON-LD</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to JSX">JSX</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Jinja2">Jinja2</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Julia">Julia</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Kotlin">Kotlin</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to LESS">LESS</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to LiveScript">LiveScript</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Lua">Lua</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Markdown">Markdown</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to mIRC">mIRC</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to MariaDB SQL">MariaDB SQL</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Mathematica">Mathematica</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Modelica">Modelica</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to MUMPS">MUMPS</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to MS SQL">MS SQL</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to mbox">mbox</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to MySQL">MySQL</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Nginx">Nginx</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to NSIS">NSIS</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to NTriples">NTriples</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Objective-C">Objective-C</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Objective-C++">Objective-C++</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to OCaml">OCaml</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Octave">Octave</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Oz">Oz</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Pascal">Pascal</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to PEG.js">PEG.js</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Perl">Perl</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to PHP">PHP</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Pig">Pig</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Plain Text">Plain Text</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to PLSQL">PLSQL</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to PostgreSQL">PostgreSQL</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to PowerShell">PowerShell</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Properties files">Properties files</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to ProtoBuf">ProtoBuf</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Python">Python</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Puppet">Puppet</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Q">Q</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to R">R</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to reStructuredText">reStructuredText</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to RPM Changes">RPM Changes</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to RPM Spec">RPM Spec</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Ruby">Ruby</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Rust">Rust</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to SAS">SAS</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Sass">Sass</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Scala">Scala</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Scheme">Scheme</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to SCSS">SCSS</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Shell">Shell</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Sieve">Sieve</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Slim">Slim</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Smalltalk">Smalltalk</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Smarty">Smarty</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Solr">Solr</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to SML">SML</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Soy">Soy</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to SPARQL">SPARQL</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Spreadsheet">Spreadsheet</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to SQL">SQL</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to SQLite">SQLite</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Squirrel">Squirrel</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Stylus">Stylus</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Swift">Swift</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to sTeX">sTeX</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to LaTeX">LaTeX</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to SystemVerilog">SystemVerilog</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Tcl">Tcl</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Textile">Textile</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to TiddlyWiki">TiddlyWiki</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Tiki wiki">Tiki wiki</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to TOML">TOML</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Tornado">Tornado</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to troff">troff</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to TTCN">TTCN</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to TTCN_CFG">TTCN_CFG</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Turtle">Turtle</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to TypeScript">TypeScript</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to TypeScript-JSX">TypeScript-JSX</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Twig">Twig</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Web IDL">Web IDL</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to VB.NET">VB.NET</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to VBScript">VBScript</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Velocity">Velocity</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Verilog">Verilog</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to VHDL">VHDL</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Vue.js Component">Vue.js Component</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to XML">XML</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to XQuery">XQuery</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Yacas">Yacas</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to YAML">YAML</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to Z80">Z80</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to mscgen">mscgen</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to xu">xu</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to msgenny">msgenny</a></li><li><a href="http://localhost:8890/edit/app.py#" title="Set language to WebAssembly">WebAssembly</a></li></ul>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="lower-header-bar"></div>


</div>

<div id="site" style="display: block; height: 591.238px;">


<div id="texteditor-backdrop">
<div id="texteditor-container" class="container"><div class="CodeMirror cm-s-ipython CodeMirror-wrap" style="height: 551.237px;"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 0px; left: 38px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true" style="display: block; bottom: 0px;"><div style="min-width: 1px; height: 1524px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 34px; margin-bottom: -15px; border-right-width: 35px; min-height: 1524px; padding-right: 15px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre class="CodeMirror-line-like"><span>xxxxxxxxxx</span></pre><div class="CodeMirror-linenumber CodeMirror-gutter-elt"><div>89</div></div></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors"><div class="CodeMirror-cursor" style="left: 4px; top: 0px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation" style=""><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">1</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">streamlit</span> <span class="cm-keyword">as</span> <span class="cm-variable">st</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">2</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">google</span>.<span class="cm-property">generativeai</span> <span class="cm-keyword">as</span> <span class="cm-variable">genai</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">3</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">4</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">5</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-comment"># Custom CSS</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">6</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">st</span>.<span class="cm-property">markdown</span>(</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">7</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-string">"""</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">8</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string"> &nbsp;  &lt;style&gt;</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">9</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string"> &nbsp; &nbsp; &nbsp;  /* Title color and font */</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">10</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string"> &nbsp; &nbsp; &nbsp;  .stTitle {</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">11</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  color: #ff5733 !important;</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">12</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  font-size: 2.5rem !important;</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">13</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  text-align: center;</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">14</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string"> &nbsp; &nbsp; &nbsp;  }</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">15</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">16</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string"> &nbsp; &nbsp; &nbsp;  /* Change button color */</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">17</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string"> &nbsp; &nbsp; &nbsp;  div.stButton &gt; button {</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">18</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  background-color: #ff4b4b;</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">19</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  color: white;</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">20</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  border-radius: 10px;</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">21</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  font-size: 16px;</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">22</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string"> &nbsp; &nbsp; &nbsp;  }</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">23</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">24</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string"> &nbsp; &nbsp; &nbsp;  /* Change sidebar color */</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">25</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string"> &nbsp; &nbsp; &nbsp;  [data-testid="stSidebar"] {</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">26</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  background-color: #f0f0f0;</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">27</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string"> &nbsp; &nbsp; &nbsp;  }</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">28</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">29</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string"> &nbsp; &nbsp; &nbsp;  /* Background Gradient */</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">30</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string"> &nbsp; &nbsp; &nbsp;  body {</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">31</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  background: linear-gradient(to right, #ffecd2, #fcb69f);</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">32</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string"> &nbsp; &nbsp; &nbsp;  }</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">33</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string"> &nbsp;  &lt;/style&gt;</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">34</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string"> &nbsp;  """</span>,</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">35</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-variable">unsafe_allow_html</span><span class="cm-operator">=</span><span class="cm-keyword">True</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">36</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">37</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">38</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">st</span>.<span class="cm-property">title</span>(<span class="cm-string">"✨ Flavour Fusion: AI-Driven Recipe Blogging ✨"</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">39</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">col1</span>, <span class="cm-variable">col2</span> <span class="cm-operator">=</span> <span class="cm-variable">st</span>.<span class="cm-property">columns</span>(<span class="cm-number">2</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">40</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">col2</span>.<span class="cm-property">write</span>(<span class="cm-string">"## Welcome to the AI-Driven Recipe Blogging App!"</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">41</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">42</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">st</span>.<span class="cm-property">markdown</span>(<span class="cm-string">"## 🥑🍕🍔🍜 AI-Generated Recipe Blogs!"</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">43</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">44</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">45</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-comment"># Initialize the Streamlit app</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">46</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">st</span>.<span class="cm-property">title</span>(<span class="cm-string">"Flavour Fusion: AI-Driven Recipe Blogging 🍽️"</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">47</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">48</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-comment"># User input for recipe topic and word count</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">49</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">topic</span> <span class="cm-operator">=</span> <span class="cm-variable">st</span>.<span class="cm-property">text_input</span>(<span class="cm-string">"Enter Recipe Topic"</span>, <span class="cm-string">"Vegan Chocolate Cake"</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">50</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">word_count</span> <span class="cm-operator">=</span> <span class="cm-variable">st</span>.<span class="cm-property">slider</span>(<span class="cm-string">"Word Count"</span>, <span class="cm-number">500</span>, <span class="cm-number">2000</span>, <span class="cm-number">1200</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">51</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">52</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-comment"># Function to generate the recipe blog using Gemini 1.5 Flash</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">53</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">def</span> <span class="cm-def">generate_recipe_blog</span>(<span class="cm-variable">topic</span>, <span class="cm-variable">word_count</span>):</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">54</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-keyword">try</span>:</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">55</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-comment"># Configure Gemini API (Replace 'YOUR_API_KEY' with your actual API key)</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">56</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-variable">genai</span>.<span class="cm-property">configure</span>(<span class="cm-variable">api_key</span><span class="cm-operator">=</span><span class="cm-string">"AIzaSyDjYLv-_SOxSluvMtABBznhQuP4DzxVaVA"</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">57</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-variable">model</span> <span class="cm-operator">=</span> <span class="cm-variable">genai</span>.<span class="cm-property">GenerativeModel</span>(<span class="cm-string">"gemini-1.5-flash"</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">58</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">59</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-comment"># Generate the blog content</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">60</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-variable">response</span> <span class="cm-operator">=</span> <span class="cm-variable">model</span>.<span class="cm-property">generate_content</span>(<span class="cm-string">f"Write a detailed blog about </span>{<span class="cm-variable">topic</span>}<span class="cm-string"> within </span>{<span class="cm-variable">word_count</span>}<span class="cm-string"> words."</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">61</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-keyword">return</span> <span class="cm-variable">response</span>.<span class="cm-property">text</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">62</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-keyword">except</span> <span class="cm-variable">Exception</span> <span class="cm-keyword">as</span> <span class="cm-variable">e</span>:</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">63</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-keyword">return</span> <span class="cm-string">f"Error: </span>{<span class="cm-variable">e</span>}<span class="cm-string">"</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">64</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">65</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-comment"># Function to generate a fun programmer joke</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">66</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">def</span> <span class="cm-def">generate_programmer_joke</span>():</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">67</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-variable">jokes</span> <span class="cm-operator">=</span> [</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">68</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-string">"Why do programmers prefer dark mode? Because light attracts bugs!"</span>,</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">69</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-string">"Why did the developer go broke? Because he used up all his cache!"</span>,</span></pre></div></div></div></div></div></div><div style="position: absolute; height: 35px; width: 1px; border-bottom: 0px solid transparent; top: 1524px;"></div><div class="CodeMirror-gutters" style="height: 1559px; left: 0px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 33px;"></div></div></div></div></div>
</div>


</div>






    


<script src="./app_files/main.min.js.download" type="text/javascript" charset="utf-8"></script>


<script type="text/javascript">
  function _remove_token_from_url() {
    if (window.location.search.length <= 1) {
      return;
    }
    var search_parameters = window.location.search.slice(1).split('&');
    for (var i = 0; i < search_parameters.length; i++) {
      if (search_parameters[i].split('=')[0] === 'token') {
        // remote token from search parameters
        search_parameters.splice(i, 1);
        var new_search = '';
        if (search_parameters.length) {
          new_search = '?' + search_parameters.join('&');
        }
        var new_url = window.location.origin + 
                      window.location.pathname + 
                      new_search + 
                      window.location.hash;
        window.history.replaceState({}, "", new_url);
        return;
      }
    }
  }
  _remove_token_from_url();
  sys_info = {"notebook_version": "6.5.4", "notebook_path": "C:\\ProgramData\\anaconda3\\Lib\\site-packages\\notebook", "commit_source": "", "commit_hash": "", "sys_version": "3.11.5 | packaged by Anaconda, Inc. | (main, Sep 11 2023, 13:26:23) [MSC v.1916 64 bit (AMD64)]", "sys_executable": "C:\\ProgramData\\anaconda3\\python.exe", "sys_platform": "win32", "platform": "Windows-10-10.0.22631-SP0", "os_name": "nt", "default_encoding": "utf-8"};
  document.addEventListener('DOMContentLoaded', function () {
    const newsId = document.querySelector('#newsId');
    const dontShowId = document.querySelector('#dontShowId');
    const showNotebookNews = localStorage.getItem('showNotebookNews');
    dontShowId.addEventListener('click', () => {
      localStorage.setItem('showNotebookNews', false);
      newsId.style.display = 'none';
    });
    if (!showNotebookNews) newsId.style.display = 'inline';
  });
</script>


</body></html>