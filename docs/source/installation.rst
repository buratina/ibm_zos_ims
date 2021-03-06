.. ...........................................................................
.. © Copyright IBM Corporation 2020                                          .
.. ...........................................................................

Installation
============

You can install the **IBM z/OS IMS collection** using one of these options:
Ansible Galaxy, private Galaxy Server or a local build.

For more information on installing collections, see `using collections`_.

.. _using collections:
   https://docs.ansible.com/ansible/latest/user_guide/collections_using.html

Ansible Galaxy
--------------
Galaxy enables you to quickly configure your automation project with content
from the Ansible community.

Galaxy provides prepackaged units of work known as collections. You can use the
`ansible-galaxy`_ command with the option ``install`` to install a collection on
your system (control node) hosted in Galaxy.

By default, the `ansible-galaxy`_ command installs the latest available
collection, but you can add a version identifier to install a specific version.
Before installing a collection from Galaxy, review all the available versions.
Periodically, new releases containing enhancements and features you might be
interested in become available.

The ansible-galaxy command ignores any pre-release versions unless
the ``==`` range identifier is set to that pre-release version.
A pre-release version is denoted by appending a hyphen and a series of
dot separated identifiers immediately following the patch version. The
**IBM z/OS IMS collection** releases collections with the pre-release
naming convention such as **1.0.0-beta2** that would require a range identifier.

Here is an example an example of installing a pre-release collection:

.. code-block:: sh

   $ ansible-galaxy collection install ibm.ibm_zos_ims:==1.0.0-beta2


If you have installed a prior version, you must overwrite an existing
collection with the ``--force`` option.

Here are a few examples of installing the **IBM z/OS IMS collection**:

.. code-block:: sh

   $ ansible-galaxy collection install ibm.ibm_zos_ims
   $ ansible-galaxy collection install -f ibm.ibm_zos_ims
   $ ansible-galaxy collection install --force ibm.ibm_zos_ims

The collection installation progress will be output to the console. Note the
location of the installation so that you can review other content included with
the collection, such as the sample playbook. By default, collections are
installed in ``~/.ansible/collections``; see the sample output.

.. _ansible-galaxy:
   https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html

.. code-block:: sh

   Process install dependency map
   Starting collection install process
   Installing 'ibm.ibm_zos_ims:1.0.0' to '/Users/user/.ansible/collections/ansible_collections/ibm/ibm_zos_ims'

After installation, the collection content will resemble this hierarchy: :

.. code-block:: sh

   ├── collections/
   │  ├── ansible_collections/
   │      ├── ibm/
   │          ├── ibm_zos_ims/
   │              ├── docs/
   │              ├── playbooks/
   │              ├── plugins/
   │                  ├── action/
   │                  ├── module_utils/
   │                  ├── modules/


You can use the `-p` option with `ansible-galaxy` to specify the installation
path, such as:

.. code-block:: sh

   $ ansible-galaxy collection install ibm.ibm_zos_ims -p /home/ansible/collections

For more information on installing collections with Ansible Galaxy,
see `installing collections`_.

.. _installing collections:
   https://docs.ansible.com/ansible/latest/user_guide/collections_using.html#installing-collections-with-ansible-galaxy

Private Galaxy server
----------------------------------------
When hosting a private Galaxy server, available content is not
always consistent with what is available on the community Galaxy server.

You can use the `ansible-galaxy`_ command with the option ``install`` to
install a collection on your system (control node) hosted on a private
Galaxy server.

By default, the ``ansible-galaxy`` command is configured to access
``https://galaxy.ansible.com`` as the server when you install a
collection. The `ansible-galaxy` client can be configured to point to a
privately running Galaxy server, by configuring the server list in
the ``ansible.cfg`` file.

Ansible searches for ``ansible.cfg`` in the following locations in this order:

   * ANSIBLE_CONFIG (environment variable if set)
   * ansible.cfg (in the current directory)
   * ~/.ansible.cfg (in the home directory)
   * /etc/ansible/ansible.cfg

To configure a Galaxy server list in the ansible.cfg file:

  * Add the server_list option under the [galaxy] section to one or more
    server names.
  * Create a new section for each server name.
  * Set the url option for each server name.

The following example shows a private running Galaxy server, and Galaxy:

.. code-block:: yaml

   [galaxy]
   server_list = galaxy, private_galaxy

   [galaxy_server.galaxy]
   url=https://galaxy.ansible.com/

   [galaxy_server.private_galaxy]
   url=https://galaxy-dev.ansible.com/
   token=<private_token>

For more configuration information, see
`configuring the ansible-galaxy client`_ and `Ansible Configuration Settings`_.

.. _configuring the ansible-galaxy client:
   https://docs.ansible.com/ansible/latest/user_guide/collections_using.html#configuring-the-ansible-galaxy-client

.. _Ansible configuration Settings:
   https://docs.ansible.com/ansible/latest/reference_appendices/config.html


Local build
-----------

You can use the ``ansible-galaxy collection install`` command to install a
collection built from source. To build your own collection, you must clone the
Git repository, build the collection archive, and install the collection. The
``ansible-galaxy collection build`` command packages the collection into an
archive that can later be installed locally without having to use Hub or
Galaxy.

To build a collection from the Git repository:

   1. Clone the sample repository:

      .. note::
         * Collection archive names will change depending on the release version.
         * They adhere to this convention **<namespace>-<collection>-<version>.tar.gz**, for example, **ibm-ibm_zos_ims-1.0.0.tar.gz**


   2. Build the collection by running the ``ansible-galaxy collection build``
   command, which must be run from inside the collection:

      .. code-block:: sh

         cd ibm_zos_ims
         ansible-galaxy collection build

      Example output of a locally built collection:

      .. code-block:: sh

         $ ansible-galaxy collection build
         Created collection for ibm.ibm_zos_ims at /Users/user/git/ibm/zos-ansible/ibm_zos_ims/ibm-ibm_zos_ims-1.0.0.tar.gz

      .. note::
         * If you build the collection with Ansible version 2.9 or earlier, you will see the following warning that you can ignore.
         * [WARNING]: Found unknown keys in collection galaxy.yml at '/Users/user/git/ibm/zos-ansible/ibm_zos_ims/galaxy.yml': build_ignore


   3. Install the locally built collection:

      .. code-block:: sh

         $ ansible-galaxy collection install ibm-ibm_zos_ims-1.0.0.tar.gz

      In the output of collection installation, note the installation path to access the sample playbook:

      .. code-block:: sh

         Process install dependency map
         Starting collection install process
         Installing 'ibm.ibm_zos_ims:1.0.0' to '/Users/user/.ansible/collections/ansible_collections/ibm/ibm_zos_ims'

      You can use the ``-p`` option with ``ansible-galaxy`` to specify the
      installation path, for example, ``ansible-galaxy collection install ibm-ibm_zos_ims-1.0.0.tar.gz -p /home/ansible/collections``.

      For more information, see `installing collections with Ansible Galaxy`_.

      .. _installing collections with Ansible Galaxy:
         https://docs.ansible.com/ansible/latest/user_guide/collections_using.html#installing-collections-with-ansible-galaxy

