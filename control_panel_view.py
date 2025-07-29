import discord

class ControlPanelView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        # Check if the user is in a voice channel.
        if not interaction.user.voice:
            return False
        # Check if the user has the manage_channels permission in the voice channel.
        return interaction.user.voice.channel.permissions_for(interaction.user).manage_channels

    @discord.ui.button(label="Ban", emoji="🚫", custom_id="ban", style=discord.ButtonStyle.danger)
    async def ban_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Create a modal to get the user to ban.
        modal = discord.ui.Modal(title="Ban User")
        modal.add_item(discord.ui.TextInput(label="User", placeholder="Mention a user to ban"))
        async def modal_callback(interaction: discord.Interaction):
            await interaction.response.defer(ephemeral=True)
            user_to_ban = modal.children[0].value
            member_to_ban = interaction.guild.get_member_named(user_to_ban)
            if member_to_ban:
                await interaction.user.voice.channel.set_permissions(member_to_ban, connect=False)
                await interaction.followup.send(f"{member_to_ban.mention} has been banned from the channel.", ephemeral=True)
            else:
                await interaction.followup.send("User not found.", ephemeral=True)
        modal.on_submit = modal_callback
        await interaction.response.send_modal(modal)

    @discord.ui.button(label="Bitrate", emoji="🎚️", custom_id="bitrate", style=discord.ButtonStyle.secondary)
    async def bitrate_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Create a modal to get the new bitrate.
        modal = discord.ui.Modal(title="Set Bitrate")
        modal.add_item(discord.ui.TextInput(label="Bitrate", placeholder="Enter a bitrate between 8000 and 96000"))
        async def modal_callback(interaction: discord.Interaction):
            await interaction.response.defer(ephemeral=True)
            bitrate = int(modal.children[0].value)
            if 8000 <= bitrate <= 96000:
                await interaction.user.voice.channel.edit(bitrate=bitrate)
                await interaction.followup.send(f"Bitrate has been set to {bitrate}.", ephemeral=True)
            else:
                await interaction.followup.send("Invalid bitrate.", ephemeral=True)
        modal.on_submit = modal_callback
        await interaction.response.send_modal(modal)

    @discord.ui.button(label="Hide", emoji="🙈", custom_id="hide", style=discord.ButtonStyle.secondary)
    async def hide_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Defer the response to prevent the interaction from timing out.
        await interaction.response.defer(ephemeral=True)
        # Toggle the visibility of the channel.
        overwrites = interaction.user.voice.channel.overwrites_for(interaction.guild.default_role)
        overwrites.view_channel = not overwrites.view_channel
        await interaction.user.voice.channel.set_permissions(interaction.guild.default_role, overwrite=overwrites)
        if overwrites.view_channel:
            await interaction.followup.send("Channel is now visible.", ephemeral=True)
        else:
            await interaction.followup.send("Channel is now hidden.", ephemeral=True)

    @discord.ui.button(label="Invite", emoji="➕", custom_id="invite", style=discord.ButtonStyle.secondary)
    async def invite_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Create a modal to get the user to invite.
        modal = discord.ui.Modal(title="Invite User")
        modal.add_item(discord.ui.TextInput(label="User", placeholder="Mention a user to invite"))
        async def modal_callback(interaction: discord.Interaction):
            await interaction.response.defer(ephemeral=True)
            user_to_invite = modal.children[0].value
            member_to_invite = interaction.guild.get_member_named(user_to_invite)
            if member_to_invite:
                await interaction.user.voice.channel.set_permissions(member_to_invite, connect=True, view_channel=True)
                await interaction.followup.send(f"{member_to_invite.mention} has been invited to the channel.", ephemeral=True)
            else:
                await interaction.followup.send("User not found.", ephemeral=True)
        modal.on_submit = modal_callback
        await interaction.response.send_modal(modal)

    @discord.ui.button(label="Limit", emoji="👥", custom_id="limit", style=discord.ButtonStyle.secondary)
    async def limit_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Create a modal to get the new user limit.
        modal = discord.ui.Modal(title="Set User Limit")
        modal.add_item(discord.ui.TextInput(label="User Limit", placeholder="Enter a user limit (0 for unlimited)"))
        async def modal_callback(interaction: discord.Interaction):
            await interaction.response.defer(ephemeral=True)
            limit = int(modal.children[0].value)
            if limit >= 0:
                await interaction.user.voice.channel.edit(user_limit=limit)
                await interaction.followup.send(f"User limit has been set to {limit}.", ephemeral=True)
            else:
                await interaction.followup.send("Invalid user limit.", ephemeral=True)
        modal.on_submit = modal_callback
        await interaction.response.send_modal(modal)

    @discord.ui.button(label="Lock", emoji="🔒", custom_id="lock", style=discord.ButtonStyle.secondary)
    async def lock_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Defer the response to prevent the interaction from timing out.
        await interaction.response.defer(ephemeral=True)
        # Toggle the lock on the channel.
        overwrites = interaction.user.voice.channel.overwrites_for(interaction.guild.default_role)
        overwrites.connect = not overwrites.connect
        await interaction.user.voice.channel.set_permissions(interaction.guild.default_role, overwrite=overwrites)
        if overwrites.connect:
            await interaction.followup.send("Channel is now unlocked.", ephemeral=True)
        else:
            await interaction.followup.send("Channel is now locked.", ephemeral=True)

    @discord.ui.button(label="Name", emoji="📝", custom_id="name", style=discord.ButtonStyle.secondary)
    async def name_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Create a modal to get the new channel name.
        modal = discord.ui.Modal(title="Set Channel Name")
        modal.add_item(discord.ui.TextInput(label="Channel Name", placeholder="Enter a new channel name"))
        async def modal_callback(interaction: discord.Interaction):
            await interaction.response.defer(ephemeral=True)
            new_name = modal.children[0].value
            voice_channel = interaction.user.voice.channel
            text_channel = discord.utils.get(interaction.guild.text_channels, name=voice_channel.name)
            await voice_channel.edit(name=new_name)
            if text_channel:
                await text_channel.edit(name=new_name)
            await interaction.followup.send(f"Channel name has been set to {new_name}.", ephemeral=True)
        modal.on_submit = modal_callback
        await interaction.response.send_modal(modal)


    @discord.ui.button(label="Transfer", emoji="🔄", custom_id="transfer", style=discord.ButtonStyle.primary)
    async def transfer_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Create a modal to get the user to transfer ownership to.
        modal = discord.ui.Modal(title="Transfer Ownership")
        modal.add_item(discord.ui.TextInput(label="User", placeholder="Mention a user to transfer ownership to"))
        async def modal_callback(interaction: discord.Interaction):
            await interaction.response.defer(ephemeral=True)
            user_to_transfer_to = modal.children[0].value
            member_to_transfer_to = interaction.guild.get_member_named(user_to_transfer_to)
            if member_to_transfer_to:
                await interaction.user.voice.channel.set_permissions(interaction.user, overwrite=None)
                await interaction.user.voice.channel.set_permissions(member_to_transfer_to, manage_channels=True, manage_roles=True)
                await interaction.followup.send(f"Ownership has been transferred to {member_to_transfer_to.mention}.", ephemeral=True)
            else:
                await interaction.followup.send("User not found.", ephemeral=True)
        modal.on_submit = modal_callback
        await interaction.response.send_modal(modal)
