
## 2022-09-05

There was no meeting. Too many people were on vacation.

## 2022-09-12

- The Steering Council and the Developer-in-Residence discussed the recent
  security releases, the Miss Islington bot, and the upcoming [PyPy/HPy
  sprint](https://www.pypy.org/posts/2022/07/ddorf-sprint-sep-2022.html).
- The SC discussed the upcoming Core Dev Sprint and what topics to bring up
  there to discuss with the Core Developers.
- The SC reviewed [PEP 669](https://peps.python.org/pep-0669/) and prepared
  some comments and questions.
- The SC discussed [non-identifier keyword
  arguments](https://github.com/python/steering-council/issues/142), and
  prepared a response.

## 2022-09-19

* The SC discussed backwards-incompatible changes done in 3.11, and possible issues with Backwards Compatibility Policy (PEP 387):
  * people need to be more aware of it
  * it's not clear that a change breaks backwards compatibility, which is a problem if more changes are added on top
* The SC decided to have a conversation about backwards compatibility at the Core Dev Sprint, to get a better feel for how core devs thank about it.
* The SC discussed release blockers for 3.11, and decided that fixes for the current issues can be postponed to 3.11.1.
* The SC agreed on a date for a meeting with Meta (fb.com) as a PSF Visionary sponsor benefit.
* The SC discussed current blockers on updating the policy for the `python` organization on GitHub.
* The SC discussed [Non-identifier keys in `**` arguments and elsewhere](https://github.com/python/steering-council/issues/142), and decided to allow them. Related details will be discussed community-wide, rather than in the SC. [See the later [Discourse topic](https://discuss.python.org/t/19293).]
* The SC discussed [PEP 692](https://peps.python.org/pep-0692/) -- using TypedDict for more precise `**kwargs` typing.


## 2022-09-26

* The SC met with Łukasz (the Developer in Residence) to discuss the
  [PyPy/HPy/GraalPy sprint](https://hpyproject.org/blog/posts/2022/09/hpy_sprint_2022_report/),
  which Łukasz attended, the relationship between HPy and CPython, and
  the possible futures of the C API.
* The SC met with Deb (the PSF Executive Director) to discuss details regarding
  the core dev sprint.
* The SC discussed bugs involving incomplete frames, like [gh-96975](https://github.com/python/cpython/issues/96975)
  and [gh-97002](https://github.com/python/cpython/issues/97002),
  and agreed with Pablo (Release Manager) that while it's a serious issue,
  it's not enough to block the 3.11.0 release.
