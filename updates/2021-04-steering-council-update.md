# April 5

- The Steering Council discussed [PEP 647: User-Defined Type
  Guards](https://www.python.org/dev/peps/pep-0647/) and approved it. An
  acceptance notice was sent. It was discussed that after Python 3.10, the
  Steering Council should start a larger discussion around the typing language
  and how it relates to the Python language.
- The Steering Council discussed [PEP 654: Exception Groups and
  except\*](https://www.python.org/dev/peps/pep-0654/) and it was decided that
  some members needed more time to review some of the existing discussion as
  well as Nathaniel's feedback.
- The Steering Council will inform the community around expectations for
  scheduling. No new features (unless straight forward) will be approved after
  the beta freeze.
- The Steering Council  discussed accepting the clarification around PyPA
  members being PEP sponsors. The commit with the proposal was merged and the
  issue was closed.
- The group discussed a response to Debian following the ongoing discussion
  around the future of the Python package in the Debian distribution and it was
  decided that Pablo would send the email to the Debian group.

# April 12

- The Steering Council discussed at length [PEP 654: Exception Groups and
  except\*](https://www.python.org/dev/peps/pep-0654/) The group decided an
  email should be sent to python-dev@ asking for more discussion and Thomas
  would draft that email.
- The group worked on the PyCon US 2021 Steering Council keynote
- Pablo mentioned he would send out the email to the Debian folks soon (which
  was sent April 13).

# April 19

- The Steering Council discussed [PEP 646: Variadic
  Generics](https://www.python.org/dev/peps/pep-0646/) and was decided that a
  decision will be postponed to after Python 3.10 as there was not enough time
  to properly evaluate the PEP given the other, more time pressing issues
  regarding [PEP 649: Deferred Evaluation Of Annotations Using
  Descriptors](https://www.python.org/dev/peps/pep-0649/) and type annotations.
- The group discussed at length some concerns raised by a group of users and
  library authors regarding that the current release of 3.10 is going to make
  life very difficult to “pydantic”, users of the library and similar libraries
  that use type annotations at runtime. This is due to some limitations in [PEP
  563: Postponed Evaluation of
  Annotations](https://www.python.org/dev/peps/pep-0563/) that affect users of
  runtime annotations (and is also related with [PEP 649: Deferred Evaluation
  Of Annotations Using
  Descriptors](https://www.python.org/dev/peps/pep-0649/)). The Steering
  Council discussed at length different possibilities with a careful evaluation
  of costs, risks and work to be done and decided that we simply can’t risk the
  compatibility breakage of PEP 563. The group decided that for stringified
  annotations the default must be reverted, at least for Python 3.10. Thomas
  will send an email to python-dev with the decision.


# April 26

- The Steering Council discussed [PEP 654: Exception Groups and
  except\*](https://www.python.org/dev/peps/pep-0654/) deciding to postpone the
  PEP to 3.11, and postpone their decision for 3.11 until after the Language
  Summit.
- The SC discussed [PEP 648: Extensible customizations of the interpreter at
  startup](https://www.python.org/dev/peps/pep-0648/), deciding to postpone it
  to 3.11.
- The SC reviewed [PEP 467: Minor API improvements for binary
  sequences](https://www.python.org/dev/peps/pep-0467/), which was postponed to
  3.11 by its author.
- The SC planned for the PyCon US keynote and Q&A, which will be recorded next
  week.
- The SC briefly discussed the notion of adding sponsor logos to
  docs.python.org.
- The SC discussed the proposal to delegate typing PEPs to a typing WG or BDFL,
  but deferred further discussion until later.
- The SC discussed the role of CODEOWNERS in CPython and how different core
  devs use the file, and the consensus was that setting expectations for both
  reviewers and PR authors could be beneficial and could help to avoid
  misunderstandings. It was decided that some devguide changes could be
  proposed.
