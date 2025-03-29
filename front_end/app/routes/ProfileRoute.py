import os
import sys
from dbmsInstance import GetDatabase
from flask import Blueprint, redirect, url_for, g, session, render_template, abort, request

profile_route = Blueprint('profile_route', __name__)

@profile_route.route('/')
def user_profile():
    # if user is not logged in redirect page not found
    if g.user is None:
        return abort(404)
    
    # Get current display name from database (TO-DO)
    currentdDisplayName = g.user.username
    
    return redirect(url_for('profile_route.user_profile_menu', displayName=currentdDisplayName))

@profile_route.route('<displayName>/Menu')
def user_profile_menu(displayName):
    # if user is not logged or username is typed directly in redirect page not found
    if g.user is None:
        return abort(404)
        
    if g.user.userType == 'Admin':
        return render_template(f'Profile/Admin/Menu.html', displayName=displayName);
    elif g.user.userType == 'Customer':
        return render_template(f'Profile/Customer/Menu.html',displayName=displayName);

    return abort(404)

@profile_route.route('<displayName>/<page>', methods=['GET', 'POST'])
def user_profile_page(displayName, page):
    # if user is not logged in redirect page not found
    if g.user is None:
        abort(404)
    
    # Get current display name from database (TO-DO)
    currentDisplayName = g.user.username
    
    # if username is typed incorrectly still log them in with their own username
    if displayName != currentDisplayName:
        return redirect(url_for('profile_route.user_profile_page', displayName=currentDisplayName, page=page), code=308)
    
    #try:        
    if g.user.userType == 'Admin':
        if page == 'PersonalInformation':
            return redirect(url_for('adminPI_route.profile_pi', displayName=currentDisplayName), code=308)
        elif page == 'Products':
            pageData = {}
        elif page == 'Analytics':
            return redirect(url_for('adminPI_route.profile_analytics', displayName=currentDisplayName), code=308)
    elif g.user.userType == 'Customer':    
        if page == 'PersonalInformation':
            pageData = {'email': currentDisplayName, 'PhoneNumber': '555-555-5555'}
        elif page == 'Orders':
            pageData = {}
        elif page == 'Wishlist':
            pageData = {}
    print(page)            
    return render_template(f'Profile/{g.user.userType}/{page}.html', displayName=currentDisplayName) #WE can refactor this into each if statement if you want to make it more readable by having more than just the pageData in fact we ill need to redirect for each one anyways.
    #except:
    #    abort(404)