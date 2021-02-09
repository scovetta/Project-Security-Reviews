### Summary
Review of the Linux Kernel’s practices and policies around how security vulnerabilities are reported to the kernel team, how those reports are processed and addressed, and how those vulnerabilities are disclosed to the public.

### Description
OSTIF, working with the team at Atredis Partners and a coalition of interested parties from the Kernel team including the Linux Foundation, Google Android, Google Cloud, and Red Hat worked together to map out the current system in place, and look for opportunities to improve upon that system to potentially improve the overall security of the kernel and to resolve potential problems with downstream projects like Android, Debian, Red Hat Enterprise Linux, Fedora, Ubuntu, CentOS, Arch, OpenSuse, and so many more.

This project involved multiple one-on-one interviews with members of the kernel team as well as representatives from the stakeholders where opportunities to investigate and address issues were discussed. Additionally, the Atredis team looked at documentation, articles, public talks, and discussions that took place over the last few years to construct a best-possible picture of the current topology and look toward standard industry practices to see how they could best inform their analysis.

### Results
Recommendation One – Keep All Security Discussions Public Instead of Private.

Atredis recommends that the Linux Kernel move to a public security bug reporting system. This is because a private reporting system runs counter to the spirit of open source generally; it opens up the project to criticism about transparency. The key reasoning behind this recommendation is that because serious security issues are resolved quickly in the kernel, and that there’s usually a long lead-time before kernel fixes make it into the various Linux distributions which erases much of the real world benefits of private reporting. The problems of keeping security reports private outweigh the potential benefits of public discussion.

Recommendation Two – CVE Reporting Should Reside with Downstream Distributions.

Atredis recommends that the downstream distributions manage CVE reporting. This is because the Linux Kernel is implemented differently across so many products that the resources required to test and trace bug findings is too broad and resource intensive. This finding is corroborated by a recent MITRE finding that because the Linux Kernel is not an end-product, CVE reporting was not designed for and is not appropriate for the Linux Kernel.

This recommendation asserts that the contributors to the various distributions know their products best and because of the practices of backporting fixes and integrating updates in a piecemeal fashion, a system where the kernel issued CVEs would not be helpful as the risk profiles of the individual distributions that admins are actually using is still unknown without more information. This means that a hypothetical kernel CVE system would produce lower-quality information than CVE reporting systems that are guided and driven by the distributions.

### External References
Reading the full report is strongly recommended. It is available for free at: https://ostif.org/wp-content/uploads/2021/01/2020-Atredis-Partners-OSTIF-Linux-Kernel-Vulnerability-Reporting-and-Remediation-Practices-Review-Report.pdf

