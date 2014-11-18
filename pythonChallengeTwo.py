# !/usr/bin/python
# coding=utf-8
#author liujinhou
#email 18070156983@163.com     
import string
original = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu  ynnjw ml rfc spj."
table=string.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
print original.translate(table)
text="map"
print text.translate(table)
raw_input()  
ALTER TABLE `user_role` ADD CONSTRAINT `user_role_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

ALTER TABLE `user_role` ADD CONSTRAINT `user_role_role_id_fk` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`);

ALTER TABLE `user_metadata` ADD CONSTRAINT `user_metadata_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

ALTER TABLE `user_permission` ADD CONSTRAINT `user_permission_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

ALTER TABLE `user_permission` ADD CONSTRAINT `user_permission_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `permission` (`id`);

ALTER TABLE `role_permission` ADD CONSTRAINT `role_permission_role_id` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`);

ALTER TABLE `role_permission` ADD CONSTRAINT `role_permission_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `permission` (`id`);

ALTER TABLE `user_permission` ADD CONSTRAINT `user_permission_grant_user_id` FOREIGN KEY () REFERENCES `user` ();

ALTER TABLE `role_permission` ADD CONSTRAINT `role_permission_grant_user_id` FOREIGN KEY (`grant_user_id`) REFERENCES `user` (`id`);

ALTER TABLE `permission` ADD CONSTRAINT `permission_widget_id` FOREIGN KEY (`widget_id`) REFERENCES `widget` (`id`);
