import admin_module as am


admin_privileges = am.Privileges(
        "can add post",
        "can delete post",
        "can ban user",
        "can reset passwords"
        )

admin = am.Admin("admin", "omeragić", 37,
              "admin.omeragic@example.com",
              admin_privileges)
admin.describe_user()
admin.privileges.show_privileges()
