# SC meeting summary - April 2022

## 2022-04-04

* Discussed CPython public C APIs with leading underscores in them as in
  [PEP-523](https://peps.python.org/pep-0523/) (Adding a frame evaluation API
  to CPython), for example, and the desire
  for perhaps a stable only within bugfixes API tier marked by semantics
  other than leading underscores (which should be reserved for private APIs).
  [Note from the future: this discussion later led to [PEP-689](https://peps.python.org/pep-0689/)
  (Unstable C API tier).]
* As to the question of should the PEP-523 APIs stay as is? General consensus
  was "yes". Less disruptive.
* Discussed clarifying a backwards compatibility policy regarding things which
  have no meaningful way to provide deprecation cycle warnings.
* Briefly discussed updates to [PEP-670](https://peps.python.org/pep-0670/)
  (Convert macros to functions in the Python C API).
* Discussed [PEP-678](https://peps.python.org/pep-0678/) (Enriching Exceptions
  with Notes), generally happy with the changes. Delaying pronouncement until
  after all of us have reread it.
* Discussed [PEP-681](https://peps.python.org/pep-0681/) (Data Class
  Transforms), how we'd defer that to typing-sig, and if we can generally avoid
  having the SC hold things up in delegation situations.
* Agreed on a cut-off for new 3.11 targeting PRs not already on the SC plate,
  the time window before beta1 is too short.
* Discussed our PyCon US keynote slot.

## 2022-04-11

* Welcomed Deb, our new PSF General Director.
* Developer in Residence Łukasz sync:
   * Happy about a successful migration to GitHub Issues!
   * Acknowledged rough edges, prioritizing those, ex: The CLA bot.
   * Musing about other workflow friction improvement we could do.
   * Dev in Res PyCon keynote planning. Steering Council will avoid
     covering the same topic.
* Director of Infrastructure Ee sync:
   * Discussed two factor authentication plans (2FA).
   * Noted hg.python.org & svn.python.org maintenance needs.
   * Discussed hiring another infrastructure person.
* Discussed possible fall core sprints organization.
* Agreed to accept [PEP-678](https://peps.python.org/pep-0678/) (Enriching
  Exceptions with Notes).
* Agreed to accept [PEP-670](https://peps.python.org/pep-0670/) (Convert macros
  to functions in the Python C API).
* Discussed PEPs that are vying for 3.11 acceptance:
   * [PEP 686](https://peps.python.org/pep-0686/) (Make UTF-8 mode default),
   * [PEP 687](https://peps.python.org/pep-0687/) (Isolating modules in the
     standard library),
   * [PEP 659](https://peps.python.org/pep-0659/) (Specializing Adaptive
     Interpreter),
   * [PEP 681](https://peps.python.org/pep-0681/) (Data Class Transforms).
* Discussed [PEP 620](https://peps.python.org/pep-0620/) (Hide implementation
  details from the C API).
* Discussed smoothing the PEP -> SC submission process: An issue template with a
  checklist is coming.
* Discussed python-dev vs Discourse expected use; deferring until after beta1.

## 2022-04-18

* Theme: PyCon PyCon PyCon
* Discussed if we can meet next week right before PyCon starts.
* Discussed our Steering Council PyCon US keynote plans.
* New Release Manager(s) for 3.12 chosen by existing RMs. Announce later.
* Discussed the upcoming PyCon Language Summit.
* Discussed PyCon Typing Summit attendance.
* Discussed [PEP-681](https://peps.python.org/pep-0681/) (Data Class
  Transforms), noted missing feedback from `attrs`. Lets make that happen.
* Discussed [PEP-686](https://peps.python.org/pep-0686/) (Make UTF-8 mode
  default), in favor with caveat of a longer deprecation timeline.
* Discussed obsoleting the Provisional API concept.
* Discussed tiered platform support.
* Randomly discussed enum syntax ideas.
* Made a lumberjack joke. It was so good this scribe forgot it.

## 2022-04-25

* Discussed GitHub Issues migration administrivia.
* Discussed our impending PyCon keynote.
* Discussed how most of us need to reread PEP-687.
* Discussed what role the python-ideas mailing list has.
* Discussed what topics we should bring up at the language summit.
* Discussed how we'd like to see PEPs discussed.
* Discussed release management team woes and bus factors.
* Discussed the new C API tier again this time called "semi-stable".
* Discussed shoving `mailcap` into [PEP-594](https://peps.python.org/pep-0594/)
  (Removing dead batteries from the standard library): unanimous yes.
* Missed a chance to discuss semi-sweet chocolate chip cookies.
* Mind you, møøse bites Kan be pretty nasti.
