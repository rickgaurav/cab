import React, {Component} from 'react';
import serialize from 'form-serialize';
import axios from 'axios';
import Cookies from 'js-cookie';
import ClassNames from 'classnames';

export default class CustomerApp extends Component {
    constructor(props) {
        super(props);
        this.submitForm = this.submitForm.bind(this);
        this.state = {
            is_submitting: false,
            show_success_message: false,
            show_error: false,
            customer_id: ''
        };
    }

    submitForm(e) {
        e && e.preventDefault() && e.stopPropagation();
        let form = document.querySelector('#customer-form');
        let params = serialize(form, {hash:true});

        params['csrfmiddlewaretoken'] = Cookies.get('csrftoken');

        this.setState({
            is_submitting: true
        });

        axios.post(
            '/api/trips/', params
        ).then((response) => {
            this.setState({
                is_submitting: false,
                show_success_message: true,
                customer_id: ''
            });
            setTimeout(()=> {
                this.setState({
                    show_success_message: false
                })
            }, 2000);
        }).catch((error) => {
            this.setState({
                is_submitting: false,
                show_error: true,
                customer_id: ''
            });
            setTimeout(()=> {
                this.setState({
                    show_error: false
                })
            }, 2000);
        });
    }

    render() {

        let button_text = this.props.is_submitting ? 'Submitting...' : 'Ride Now';
        let classes = ClassNames('form-group', {
            'has-feedback has-success': this.props.show_success_message,
            'has-feedback has-error': this.props.show_error
        });

        return (
            <div>
                <div className="col-xs-4 perfect-centering">
                    <h2>Book a Ride</h2>
                    <form id="customer-form">
                        <div className={classes}>
                            <label>Customer Id</label>
                            <input type="text" className="form-control" id="focusedInput" name="customer"/>
                        </div>
                        <button type="submit" className="btn btn-primary" onClick={this.submitForm}>
                            {button_text}
                        </button>
                    </form>
                    {
                        this.state.show_success_message &&
                        <div className="alert alert-success alert-container" role="alert">
                          Yayyy!! Request Submitted
                        </div>
                    }
                    {
                        this.state.show_error &&
                        <div className="alert alert-danger alert-container" role="alert">
                          Oh Ohhh!! Request Failed. Try Again
                        </div>
                    }
                </div>

            </div>
        );
    }
}
