from os.path import basename, exists, join
from ansible.plugins.vars.host_group_vars import VarsModule as HostGroupVarsModule
from ansible.utils.vars import combine_vars


class VarsModule(HostGroupVarsModule):
    """
    Vars plugin to read variables from "stage_vars" path relative to playbook.
    """

    REQUIRES_WHITELIST = True

    # Auto detected stage name
    _stage = None

    # Path to inventory
    _inventory_path = None

    def get_vars(self, loader, path, entities, cache=True):
        """
        This function is called by ansible six times, in the following order:

        * Inventory, for "all" group
        * Playbook, for "all" group
        * Inventory, for other groups
        * Playbook, for other groups
        * Inventory, for host
        * Playbook, for host

        If Inventory and Playbook live in the same directory, return nothing.
        """

        if VarsModule._inventory_path is None:
            # On first run, use last part of inventory path as stage name.
            VarsModule._stage = basename(path)
            VarsModule._inventory_path = path
            return {}

        if VarsModule._inventory_path == path:
            # Do nothing if run on inventory path.
            return {}

        get_vars = lambda p: super(VarsModule, self).get_vars(loader, p, entities, cache)

        return combine_vars(
            get_vars(join(path, "stage_vars", "all")),
            get_vars(join(path, "stage_vars", VarsModule._stage)),
        )
