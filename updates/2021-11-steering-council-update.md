# November 1

- The SC discussed [PEP 649 -- Deferred Evaluation Of Annotations
  Using Descriptors](https://www.python.org/dev/peps/pep-0649/) & [PEP 563 --
  Postponed Evaluation of
  Annotations](https://www.python.org/dev/peps/pep-0563/). The SC decided it
  would tell the community that more information is needed. Barry will draft
  an email explaining the current situation and calling for help from static
  and dynamic typing users.
- The SC reviewed the open issues in the public Steering Council
  repo: https://github.com/python/steering-council/issues.
- The SC discussed SC promotion during the call for nomination
  period, which started on Nov 1.
- The SC discussed [PEP 663 - Standardizing Enum str(), repr(),
  and format() behaviors](https://www.python.org/dev/peps/pep-0663/) and that
  Barry would write the rejection draft.
- Brett informed the SC of an issue involving the return type of iterators and
  the SC decided it would continue discussing it at the next meeting
  (https://bugs.python.org/issue45250).

# November 8

- The SC had their bi-weekly meeting with the
  Developer-in-Residence. Received an update from Łukasz on what he is working
  on.
- The SC discussed  [PEP 663 - Standardizing Enum str(), repr(),
  and format() behaviors](https://www.python.org/dev/peps/pep-0663/) and after
  some initial discussion, it was decided that it needs more discussion on
  python-dev@.
- The SC discussed [PEP 467 -- Minor API improvements for binary
  sequences](https://www.python.org/dev/peps/pep-0467/). `bchr()` was taken out
  like the SC had requested and then an `ascii()` method was added in without
  any mention. Pablo will draft a response.
- [PEP 554 -- Multiple Interpreters in the
  Stdlib](https://www.python.org/dev/peps/pep-0554/) was discussed. A proof of
  concept is needed and the SC is not yet ready to review the PEP without it.

# November 15

- The SC met with Ezio and got an update on what Ezio was working
  on. SC told Ezio not to be overly concerned with perfection and not to strive
  for it. The SC gave Ezio a deadline of Dec 7th to get everything migrated
  over.
- The SC discussed a PR to the CPython repo regarding `__iter__`
  and iterators being inconsistently required by CPython
  (https://github.com/python/cpython/pull/29170). The SC's decision was to
  update the definitions to say it's a CPython implementation detail that it is
  inconsistent in its checking whether what an iterable returns is a proper
  iterator or not (i.e. keep the `__iter__` requirement but admit it isn't
  rigorously enforced by CPython as a historical accident). Brett committed
  updates to the PR.
- The SC discussed a pull request in the “python/voters”
  repository that allows core devs to trigger automerge behavior from labels
  and decided it is fine to merge.
- Carol gave an update on the documentation WG: The WG is going to a series of
  1 hour monthly meetings and then do the rollout next year.
- Barry updated the text for the PEP 663 rejection and sent it out to python-dev@.
- Group reviewed text for "The current state of typing PEPs" (i.e. request for
  PEP 563 and 649) and [Barry sent it to python-dev@](https://mail.python.org/archives/list/python-dev@python.org/message/VIZEBX5EYMSYIJNDBF6DMUMZOCWHARSO/).
- The SC reviewed PEP 646 (Variadic Generics) and Barry sent the
  approval to the PEP team.
- The SC discussed how notes will be taken after Ewa leaves.
- The SC discussed PEP 518 (Specifying Minimum Build System
  Requirements for Python Projects) and how some folks are split on toml.

# November 22

- The SC met with Łukasz and received an update from Łukasz on
  his recent work. Additionally, the SC informed Łukasz he should work on
  upgrading the CLA process. Łukasz will reach out to Yury and Ezio.
- The SC discussed Victor's request to remove `asynchat` and
  friends prematurely. The SC decided that the removal of `asynchat` needs to
  wait another 6 months.
- The SC discussed Ethan's email to the SC asking about the `re`
  module and its RegexFlag.
- The SC discussed the exception for `Py_SET_TYPE` request. Pablo
  will write a response to Petr request stating that the change needs to be
  rolled back in case there are any issues and they need to document any
  breakage in 3.11.
- The SC discussed the various questions pertaining to the
  current state of typing PEPs. Thomas will draft a response to Chris and
  Paul's questions and the group discussed Barry's private conversation with a
  core dev about this as well.
- The SC decided that it should be the 2022 SC that decides what
  happens to python-dev@.

# November 29

- The SC met with Ezio. The date to do the full migration has
  been pushed to mid-January. By Dec 7th, Ezio will put all issues into a test
  repo for python-dev to test and then the migration will happen when Steffen
  from GitHub returns from vacation in January.
- The SC discussed [PEP 659 - Specializing Adaptive
  Interpreter](https://www.python.org/dev/peps/pep-0659/) and whether or not it
  should be a PEP. It was determined that the informational aspect of the writeup
  is lacking such as how trade-offs are decided. The SC also discussed how different
  companies working on Python should work especially in terms of transparency. For the
  time being there will be no communications about this to the PEP authors or
  the community as the SC wants to discuss this further. This discussion will
  continue with the new SC as well.

## Discussing PEPs in Threads Listed in the `Post-History` Header

- Review the PEP's `Post-History` header for discussion threads.
- Discuss PEPs in the appropriate threads to gather community feedback and insights.
- Emphasize the importance of community feedback and discussion.
