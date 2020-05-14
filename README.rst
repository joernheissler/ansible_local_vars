#########################
ansible stage_vars plugin
#########################

.. code-block:: bash

    ansible-playbook -i inventory/prod project/foo/playbook.yml

This plugin assumes that you're using multiple inventories, structured like ``inventory/<stage>/``,
and that playbooks and inventories live in separate paths.

The `variable precedence <https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable>`__ is changed to:

* ...
* inventory file or script group vars
* inventory ``group_vars/all``
* playbook ``group_vars/all``
* playbook ``stage_vars/all/group_vars/all``
* playbook ``stage_vars/<stage>/group_vars/all``
* inventory ``group_vars/*``
* playbook ``group_vars/*``
* playbook ``stage_vars/all/group_vars/*``
* playbook ``stage_vars/<stage>/group_vars/*``
* inventory file or script host vars
* inventory ``host_vars/*``
* playbook ``host_vars/*``
* playbook ``stage_vars/all/host_vars/*``
* playbook ``stage_vars/<stage>/host_vars/*``
* ...
