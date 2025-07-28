from users_module import Admin, Privileges

admin_privileges = Privileges(
        "can add post",
        "can delete post",
        "can ban user",
        "can reset passwords"
        )

admin = Admin("admin", "omeragić", 37,
              "admin.omeragic@example.com",
              admin_privileges)
admin.describe_user()
admin.privileges.show_privileges()
