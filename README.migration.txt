# Time-stamp: <2025-10-14 07:42:37 rene>

On uberspace:
pip3.13 install django==5.2.7
pip3.13 install django-countries

On uberspace after tdjs dist prod/test:
rm tangodjsforgoodsound/migrations/0011_alter_dj_since.py
./tdjs dbc
./tdjs dbm
./tdjs dba

