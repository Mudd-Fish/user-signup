#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi


class MainHandler(webapp2.RequestHandler):
    def get(self):

        header = "<h1>User Signup</h1>"

        user = """
        <form action="/uservalidation" method="post">

            <label>
                Username: <input type="text" name="username"/>
            </label>
            <br>

            <label>
                Password: <input type="text" name="password"/>
            <label>
            <br>

            <label>
                Password Verification: <input type="text" name="password_verify"/>
            </label>
            <br>

            <label>
                Email (optional): <input type="text" name="email"/>
            </label>
            <br>

            <input type=submit>
        </form>
        """

        content = header + user

        self.response.write(content)

class uservalidation(webapp2.RequestHandler):

    def post(self):
        print(self)
        user = self.request.get("username")
        print(user)
        if (not user) or (user.strip() == ""):
            error = "Please Fill Out This Field"
            self.redirect("/?error" + cgi.escape(error, quote=True))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/uservalidation', uservalidation)
], debug=True)
