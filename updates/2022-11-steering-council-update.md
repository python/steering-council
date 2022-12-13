## 2022-11-07

- The Steering Council met with Łukasz  (the Developer-in-Residence). There has been some issue with the recent OpenSSL CVE as some of the bots that
  are running on Heroku needed to be restarted to pick up the patched version of
  OpenSSL. Unfortunately, some of the bots never came back to life after the
  restart. Łukasz is investigating.
- We have been informed that we are lagging a bit with the merging pending accepted Pull Requests.
  Łukasz is going to help with the merges and the backports. Łukasz also thinks
  that making auto-merge nicer may help here.
-  The Steering Council and the developer in residence
  discussed several things that can be done to improve this situation such as using GitHub Actions
  or collecting a bunch of search URLs to help people find these PRs.
- The Steering Council discussed the timeline for the Steering Council Elections. The group asked
  Ee to prepare to start the process with a similar timeline as previous years: 2
  weeks + 1 week in between + 2 weeks (nominations + discussion + election).
- The Steering Council discussed some remaining aspects of [PEP 669 – Low Impact
  Monitoring for CPython](https://peps.python.org/pep-0669/) and decided to accept
  it.
- The Steering Council discussed some performance aspects of [PEP 683 – Immortal Objects](https://peps.python.org/pep-0683/).

## 2022-11-14

- The Steering Council discussed [PEP 649: Deferred Evaluation Of Annotations Using Descriptors](https://www.python.org/dev/peps/pep-0649/)
  and agreed to announce that the Steering Council is ready to tentatively
  accept the PEP. The announcement was [done in a discourse
  thread](https://discuss.python.org/t/pep-649-deferred-evaluation-of-annotations-tentatively-accepted/21331)
- The Steering Council discussed [PEP 690 – Lazy Imports](https://peps.python.org/pep-0690/) and decided to reject it. The rejection
  notice [was posted on Discourse](https://discuss.python.org/t/pep-690-lazy-imports-again/19661/26)

## 2022-11-21

- The Steering Council met with the developer in residence (Łukasz) to discuss progress. Most
  of Łukasz's time was spent setting up a new machine for bigmem buildbots and
  Windows debugging/development.
- The Steering Council discussed the next steps for encouraging mentorship.
- The Steering Council approved (did not veto) new core developers -- Hugo van Kemenade & Kumar Aditya.
- The Steering Council discussed concerns about the process for new core devs (regarding how
  public comments may affect the candidate in different ways). The group
  agreed that as changing this process is not in the Steering Council mandate, the discussion
  should be taken elsewhere.
- The Steering Council reviewed pending communication action items.
- The Steering Council discussed [PEP 692 – Using TypedDict for more precise **kwargs typing](https://peps.python.org/pep-0692/), and decided that it could be accepted without the syntax change. 
- The Steering Council accepted clarifications to [PEP 646 – Variadic Generics](https://peps.python.org/pep-0646/)

## 2022-11-28

- The Steering Council continued discussing [PEP 692 – Using TypedDict for more precise **kwargs typing](https://peps.python.org/pep-0692/)
  and noted that the PEP has not been updated yet to reflect the previous requests from the Steering Council. Thomas will ask the authors
  to update the PEP to remove the syntax change and its related dunder method.
- The Steering Council discussed what is the correct place for [PEP 659 – Specializing Adaptive Interpreter](https://peps.python.org/pep-0659/).
- The Steering Council discussed how the creation of manylinux wheels for 3rd party packages worked on the 3.11 release. The group agreed that
  we want to encourage the maintainers of these packages to create wheels for new versions as soon as possible in the release cycle (after the first
  beta) as this will allow the community to test new versions faster and sooner. The group discussed how the core team and the Steering Council
  can try to improve the situation. Pablo will write (as Release Manager, not Steering Council member) a communication draft about what our point
  of view is so we can publish it on our communication channels.
- The Steering Council discussed very briefly [PEP 620 – Hide implementation details from the C API](https://peps.python.org/pep-0620/) and noted that it
  has not yet been submitted to the Steering Council formally and is still marked as a draft. 
- The Steering Council started discussing the problems that will happen when OpenSSL 3 is the only supported option. A [thread on discourse](https://discuss.python.org/t/our-future-with-openssl/21486/73)
  was created about this.
