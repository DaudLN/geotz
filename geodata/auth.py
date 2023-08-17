import strawberry
from gqlauth.user import arg_mutations as authmutations
from gqlauth.user.queries import UserQueries


@strawberry.type
class AuthQuery(UserQueries):
    # you can add your queries here
    ...


@strawberry.type
class AuthMutation:
    verify_token = authmutations.VerifyToken.field
    update_account = authmutations.UpdateAccount.field
    archive_account = authmutations.ArchiveAccount.field
    delete_account = authmutations.DeleteAccount.field
    password_change = authmutations.PasswordChange.field
    token_auth = authmutations.ObtainJSONWebToken.field
    register = authmutations.Register.field
    verify_account = authmutations.VerifyAccount.field
    resend_activation_email = authmutations.ResendActivationEmail.field
    send_password_reset_email = authmutations.SendPasswordResetEmail.field
    password_reset = authmutations.PasswordReset.field
    password_set = authmutations.PasswordSet.field
    refresh_token = authmutations.RefreshToken.field
    revoke_token = authmutations.RevokeToken.field
