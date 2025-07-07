# Apply iptables rules to restrict external access
Usually, in various projects, iptables configuration is done along with preparing and hardening, but considering that in the task sent from you, it was requested separately, we will write a role only for iptables.
This is a better option than shell scripting in terms of flexibility and idempotency.
### About this role
This Ansible role is designed to automate the installation and configuration of Docker. It provides a streamlined way to set up Docker on multiple systems with consistent settings.

Features:
--------------
- install iptables-persistent
- configure iptables

Role Variables
--------------
All variables used in this role are located in the default directory of the role. You can find and modify them in the `roles/iptables/defaults/main.yml`
These variables allow you to customize iptables and configuration based on your requirements. Simply update the variables in this file to tailor the role's behavior to your environment.

Example Playbook
----------------

You can use the iptables role in a playbook like the example below to configure iptables:

    - name: configure iptables
      hosts: all
      become: true
      gather_facts: true
      roles:
        - ../roles/iptables
### Test and verification

