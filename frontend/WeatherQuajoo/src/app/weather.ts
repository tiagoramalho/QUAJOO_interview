import { Component, OnInit} from '@angular/core';
import {Subscription} from 'rxjs/Subscription';
import {WeatherApiService} from './weather-api.service';
import {City} from './city.model';
import { Location } from '@angular/common';
import citiesData from '../assets/formated_city_list.json';
import {HttpHeaders, HttpClient, HttpErrorResponse} from '@angular/common/http';


@Component({
    selector: 'app-weather',
    templateUrl: './weather.component.html',
    styleUrls: ['./weather.component.css'],
})
export class AppComponent implements OnInit {
    title = 'app';
    cityListSubs: Subscription;
    cityList: City[];
    citiesJson: any = citiesData;
    c: any;


    constructor(private cityApi: WeatherApiService, private location: Location, private http: HttpClient) {
    }

    ngOnInit() {
        this.cityApi
            .getCities()
            .subscribe(cities => {
                this.cityList = cities;
                console.log(this.cityList);
            });
    }

    onSave(cityId) {
        console.log(cityId);
        this.http.post('http://127.0.0.1:5000/city',
            {
                open_id: cityId
            })
            .subscribe(
                data  => {
                    console.log('POST Request is successful ', data);
                    this.pageRefresh();
                    return true;
                },
                error  => {

                    console.log('Error', error);
                    return false;

                }

            );
    }

    pageRefresh() {
        location.reload();
    }

}
