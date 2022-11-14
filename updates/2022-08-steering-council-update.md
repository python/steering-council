# SC meeting summary - August 2022

## 2022-08-01

* The Steering Council met with the Developer-in-Residence (Łukasz) and discussed:
    * The status of the 3.11 release
    * the asyncio uncancel issue
    * The number of last-minute bugs and issues that we are experiencing
* The SC discussed the fall Core Dev Sprint with the PSF Executive
  Director, as well as plans for another Developer-in-Residence and
  offering mentoring support to core developers.
* The SC discussed the Python 3.11 release and the approximate cause of the
  release blockers, as well as how to improve the situation in the future
  and how to gather feedback for future release managers.

## 2022-08-08

* The SC discussed the status and next steps for CVE-2020-10735: Prevent DoS by
  large int<->str conversions. 
* Pablo asked the Docs working group for assistance with the 3.11 release
  notes.
* The SC discussed the status of the repo for planet.python.org. The SC will
  ask Ee about moving the planet repo over to the PSF organization.
* The SC discussed how to move forward with the future of type annotations
  ([PEP 563 – Postponed Evaluation of
  Annotations](https://peps.python.org/pep-0563/) and [PEP 649 – Deferred
  Evaluation Of Annotations Using
  Descriptors](https://peps.python.org/pep-0649/)). Several maintenance
  considerations and deprecation strategies were considered, listing things
  that would break and ways to overcome the challenges.
* The SC discussed the state of [PEP 2 – Procedure for Adding New
  Modules](https://peps.python.org/pep-0002/), [PEP 4 – Deprecation of Standard
  Modules](https://peps.python.org/pep-0004/), and [PEP 411  – Provisional
  packages in the Python standard library](https://peps.python.org/pep-0411/).
  The SC decided to email the community to see if they think we should have
  separate policy documents from PEP.
* The SC discussed asking the platform release managers (Ned and Steve) to
  document their side of the release process to reduce the bus factor and
  search for more automation possibilities.

## 2022-08-15

* The SC met with the Developer in Residence and discussed:
    * Fixing blockers for the 3.11.0rc1 release
    * An update of the CLA bot, and a future update to EdgeDB 2.0
    * Possible candidates for blog posts for the community
* The SC met with the PSF Executive Director and discussed the organization
  of the 2022 Core Dev sprints.
* The SC discussed the logistics of having a meeting with Meta as part of
  the Visionary sponsor relationship.
* The SC discussed encouraging projects to release wheels for Release
  Candidates of new minor versions and what challenges are being faced by
  users and maintainers. Several possible proposals were listed, including
  asking NumFocus and other organizations for assistance.


## 2022-08-22

* The SC briefly discussed [PEP 649 – Deferred Evaluation Of Annotations Using
  Descriptors](https://peps.python.org/pep-0649/) and what is left to decide.
* The SC discussed several aspects of the upcoming core dev sprint.
* The SC discussed planning of the meeting with Meta as a PSF Visionary sponsor
  benefit.
* The SC discussed possibly delaying 3.11.0 due to a timing conflict with
  release managers and the core dev sprint and life in general. It was agreed
  that it is ok to delay 3.11.0 until the 24th of October.
* The SC confirmed that 3.12alpha1 is still intended during the dev sprint.
* As a way to improve the testing of new versions, Brett noted he's planning to
  work to improve GitHub CI configs to make it more likely for users to test
  against release candidates and betas and to make it obvious how to do it.
* The SC discussed the migration concerns raised from the proposed migration
  for PEP discussion from python-dev to discuss.python.org migration. The SC
  noted that documentation work remains before making it fully official. Also,
  we won't shut down the python-dev list, but we expect PEP authors to not pay
  attention to it when discussing PEPs.
* The SC discussed the possibility of inviting some non-core devs to the sprint
  and we agreed that a goal of focus is key for a successful sprint.
* The SC discussed what to do with PEPs that are not regular enhancement
  proposals nor informative documents (like
  https://peps.python.org/pep-0659/). The SC decided that for [PEP 659–
  Specializing Adaptive Interpreter](https://peps.python.org/pep-0659/)  in
  particular the status should be Final.
* The SC agreed that we want to avoid having people write a PEP after pushing
  through an implementation.
* The SC discussed CPython's backward compatibility policy and decided that we
  should gather input from the core devs on that. It was proposed to ask people
  attending the core dev sprint as a first measure.

## 2022-08-29

* The SC met with the Developer in Residence and discussed:
    * Bot/CLA hosting and Heroku tiers.
    * EdgeDB update for the CLA bot.
    * Blog posts and talk ideas.
    * Typing PEPs.
* The SC discussed details about the organization of the 2022 Core Dev sprints.
* The SC discussed resources for mentoring and how to help core devs mentor new
  contributors.
* The SC discussed [PEP 674 – Disallow using macros as
  l-values](https://peps.python.org/pep-0674/) and the changes that were merged
  without a PEP accepted in 3.11. Pablo will answer [to the discussion that
  Victor started in
  discourse](https://discuss.python.org/t/pep-674-disallow-using-macros-as-l-values-and-python-3-11/18297/14).
* The SC discussed several aspects on how to deal with breaking changes. It was
  decided that this will be a discussion point with the rest of the core devs
  in the core dev sprint.
